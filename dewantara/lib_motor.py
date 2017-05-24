########################################################################################################################
# Perintah untuk menggerakan motor dengan input pixel X, Y
########################################################################################################################


def motor_input(conn, conn1, bentuk):
    while True:
        masukan = conn.recv()
        conn1.send(masukan)
        x = masukan.__getitem__(0)
        y = masukan.__getitem__(1)
        shape = masukan.__getitem__(4)
        if bentuk == shape:
            print('cX=', x, 'cY=', y, 'shape=', shape)
        else:
            print("")
