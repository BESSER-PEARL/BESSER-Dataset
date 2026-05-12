




import java.time.LocalDateTime;

import java.util.List;
import java.util.ArrayList;

public class Transacci_n  {

    private float monto;
    private LocalDateTime fecha;
    private String detalle;
    private int id;





    private Cuenta_external cuenta_external;




    private Cuenta_external cuenta_external;


    public Transacci_n(
        float monto,        LocalDateTime fecha,        String detalle,        int id    ) {
        this.monto = monto;
        this.fecha = fecha;
        this.detalle = detalle;
        this.id = id;
    }


    public float getMonto() {
        return monto;
    }

    public void setMonto(float monto) {
        this.monto = monto;
    }
    public LocalDateTime getFecha() {
        return fecha;
    }

    public void setFecha(LocalDateTime fecha) {
        this.fecha = fecha;
    }
    public String getDetalle() {
        return detalle;
    }

    public void setDetalle(String detalle) {
        this.detalle = detalle;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Cuenta_external getCuenta_external() {
        return cuenta_external;
    }

    public void setCuenta_external(Cuenta_external cuenta_external) {
        this.cuenta_external = cuenta_external;
    }
    public Cuenta_external getCuenta_external() {
        return cuenta_external;
    }

    public void setCuenta_external(Cuenta_external cuenta_external) {
        this.cuenta_external = cuenta_external;
    }

}