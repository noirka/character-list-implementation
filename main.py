#!/usr/bin/env python3
"""
Демонстрація роботи з двобічно зв'язаним списком
"""

from src.doubly_linked_list import DoublyLinkedList


def main():
    print("=== Демонстрація роботи Character List Implementation ===\n")
    
    char_list = DoublyLinkedList()
    print("1. Створено порожній список")
    print(f"   Довжина: {char_list.length()}")
    
    print("\n2. Додавання елементів в кінець:")
    for char in "HELLO":
        char_list.append(char)
        print(f"   Додано '{char}', список: {char_list.to_list()}")
    
    print("\n3. Вставка елементів:")
    char_list.insert('X', 0)  
    print(f"   Вставлено 'X' на позицію 0: {char_list.to_list()}")
    char_list.insert('Y', 3)  
    print(f"   Вставлено 'Y' на позицію 3: {char_list.to_list()}")
    
    print("\n4. Отримання елементів:")
    print(f"   Елемент на позиції 0: '{char_list.get(0)}'")
    print(f"   Елемент на позиції 3: '{char_list.get(3)}'")
    
    print("\n5. Пошук елементів:")
    print(f"   Перший індекс 'L': {char_list.findFirst('L')}")
    print(f"   Останній індекс 'L': {char_list.findLast('L')}")
    print(f"   Індекс 'Z' (відсутній): {char_list.findFirst('Z')}")
    
    print("\n6. Видалення за індексом:")
    deleted = char_list.delete(0)
    print(f"   Видалено елемент на позиції 0: '{deleted}'")
    print(f"   Список після видалення: {char_list.to_list()}")
    
    char_list.append('L')
    char_list.append('L')
    print(f"\n7. Додано дублікати 'L': {char_list.to_list()}")
    
    char_list.deleteAll('L')
    print(f"   Після видалення всіх 'L': {char_list.to_list()}")
    
    print("\n8. Копіювання списку:")
    cloned_list = char_list.clone()
    print(f"   Оригінал: {char_list.to_list()}")
    print(f"   Копія: {cloned_list.to_list()}")
    
    print("\n9. Обернення списку:")
    char_list.reverse()
    print(f"   Після обернення: {char_list.to_list()}")
    
    print("\n10. Розширення списку:")
    extension_list = DoublyLinkedList()
    for char in "WORLD":
        extension_list.append(char)
    print(f"    Список для розширення: {extension_list.to_list()}")
    char_list.extend(extension_list)
    print(f"    Після розширення: {char_list.to_list()}")
    
    print("\n11. Очищення списку:")
    print(f"    Довжина до очищення: {char_list.length()}")
    char_list.clear()
    print(f"    Довжина після очищення: {char_list.length()}")
    print(f"    Список після очищення: {char_list.to_list()}")
    
    print("\n=== Демонстрація завершена ===")


if __name__ == "__main__":
    main()
