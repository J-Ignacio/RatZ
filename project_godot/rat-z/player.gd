extends CharacterBody2D

const SPEED = 500.0        # Un poquito más rápido para notar el arranque
const JUMP_VELOCITY = -600.0 # Salto más alto para que sea obvio
var gravity = 1200         # Gravedad más pesada para que caiga rápido

func _physics_process(delta):
	# 1. GRAVEDAD
	if not is_on_floor():
		velocity.y += gravity * delta

	# 2. MOVIMIENTO (Usando teclas físicas universales)
	var direction = 0
	if Input.is_physical_key_pressed(KEY_A) or Input.is_physical_key_pressed(KEY_LEFT):
		direction -= 1
	if Input.is_physical_key_pressed(KEY_D) or Input.is_physical_key_pressed(KEY_RIGHT):
		direction += 1
	
	velocity.x = direction * SPEED

	# 3. SALTO
	if (Input.is_physical_key_pressed(KEY_SPACE) or Input.is_physical_key_pressed(KEY_W)) and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# 4. LA LÍNEA MÁGICA
	move_and_slide()
	
	# TEST: Si esto sale en la consola, el teclado está vivo
	if direction != 0:
		print("TECLADO DETECTADO: Moviéndose a ", velocity.x)
