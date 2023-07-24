def luna_weight(earth_weight):
    lunar_gravity = 1/6
    lunar_weight = earth_weight * lunar_gravity
    return lunar_weight
    
earth_weight = float(input("Введите вашу массу на Земле (в килограммах): "))
lunar_weight = luna_weight(earth_weight)
print(f"Ваш лунный вес составит примерно {lunar_weight:.2f} килограмма.")
