from menu_data import csv_text

def parse_csv(text):
    """Parses the CSV string into a list of item dictionaries."""
    items = []
    for line in text.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split(',')
        if len(parts) == 4:
            category, name, quantity, price_str = parts
            price = float(price_str.replace('$', ''))
            items.append({
                'category': category.strip(),
                'name': name.strip(),
                'quantity': quantity.strip(),
                'price': price
            })
    return items

def group_by_category(items):
    """Groups items by category while preserving their relative order."""
    groups = {}
    for item in items:
        cat = item['category']
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(item)
    return groups

def format_menu(items):
    """Formats the menu items according to lab specifications."""
    groups = group_by_category(items)
    output_lines = []
    
    for category, cat_items in groups.items():
        # Capitalize category name for the header
        header = f"- {category.capitalize()} Items *"
        output_lines.append(header)
        
        for item in cat_items:
            # Apply the 1.8 price multiplier and format to 2 decimal places
            calculated_price = item['price'] * 1.8
            price_formatted = f"${calculated_price:.2f}"
            
            # Construct the line with proper indentation and tab separation
            line = f" {price_formatted}\t{item['name']}, {item['quantity']}"
            output_lines.append(line)
        
        output_lines.append("") # Blank line between categories
        
    return "\n".join(output_lines).strip()

def main():
    items = parse_csv(csv_text)
    formatted_menu = format_menu(items)
    print(formatted_menu)

if __name__ == "__main__":
    main()