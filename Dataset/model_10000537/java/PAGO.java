





import java.util.List;
import java.util.ArrayList;

public class PAGO  {

    private String Type_of_payment;





    private Informacion_Primaria informacion_primaria;




    private Gestion_de_Limpieza gestion_de_limpieza;




    private Dispensador_de_dinero dispensador_de_dinero;




    private Usuario usuario;


    public PAGO(
        String Type_of_payment    ) {
        this.Type_of_payment = Type_of_payment;
    }


    public String getType_of_payment() {
        return Type_of_payment;
    }

    public void setType_of_payment(String Type_of_payment) {
        this.Type_of_payment = Type_of_payment;
    }

    public Informacion_Primaria getInformacion_primaria() {
        return informacion_primaria;
    }

    public void setInformacion_primaria(Informacion_Primaria informacion_primaria) {
        this.informacion_primaria = informacion_primaria;
    }
    public Gestion_de_Limpieza getGestion_de_limpieza() {
        return gestion_de_limpieza;
    }

    public void setGestion_de_limpieza(Gestion_de_Limpieza gestion_de_limpieza) {
        this.gestion_de_limpieza = gestion_de_limpieza;
    }
    public Dispensador_de_dinero getDispensador_de_dinero() {
        return dispensador_de_dinero;
    }

    public void setDispensador_de_dinero(Dispensador_de_dinero dispensador_de_dinero) {
        this.dispensador_de_dinero = dispensador_de_dinero;
    }
    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

}