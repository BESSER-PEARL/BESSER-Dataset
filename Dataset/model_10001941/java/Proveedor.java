





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String nit;
    private String direccion;
    private String razonSocial;
    private String telefono;



    public Proveedor(
        String nit,        String direccion,        String razonSocial,        String telefono    ) {
        this.nit = nit;
        this.direccion = direccion;
        this.razonSocial = razonSocial;
        this.telefono = telefono;
    }


    public String getNit() {
        return nit;
    }

    public void setNit(String nit) {
        this.nit = nit;
    }
    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }


}