





import java.util.List;
import java.util.ArrayList;

public class CONTACTO  {

    private String CORREO;
    private String NOMBRE;





    private LIBRO_DE__DIRECCIONES libro_de__direcciones;




    private FOTO foto;


    public CONTACTO(
        String CORREO,        String NOMBRE    ) {
        this.CORREO = CORREO;
        this.NOMBRE = NOMBRE;
    }


    public String getCorreo() {
        return CORREO;
    }

    public void setCorreo(String CORREO) {
        this.CORREO = CORREO;
    }
    public String getNombre() {
        return NOMBRE;
    }

    public void setNombre(String NOMBRE) {
        this.NOMBRE = NOMBRE;
    }

    public LIBRO_DE__DIRECCIONES getLibro_de__direcciones() {
        return libro_de__direcciones;
    }

    public void setLibro_de__direcciones(LIBRO_DE__DIRECCIONES libro_de__direcciones) {
        this.libro_de__direcciones = libro_de__direcciones;
    }
    public FOTO getFoto() {
        return foto;
    }

    public void setFoto(FOTO foto) {
        this.foto = foto;
    }

}