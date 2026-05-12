





import java.util.List;
import java.util.ArrayList;

public class CuentaBanco  {

    private String tipoCuenta;
    private String nombreBanco;
    private String numeroCuenta;



    public CuentaBanco(
        String tipoCuenta,        String nombreBanco,        String numeroCuenta    ) {
        this.tipoCuenta = tipoCuenta;
        this.nombreBanco = nombreBanco;
        this.numeroCuenta = numeroCuenta;
    }


    public String getTipocuenta() {
        return tipoCuenta;
    }

    public void setTipocuenta(String tipoCuenta) {
        this.tipoCuenta = tipoCuenta;
    }
    public String getNombrebanco() {
        return nombreBanco;
    }

    public void setNombrebanco(String nombreBanco) {
        this.nombreBanco = nombreBanco;
    }
    public String getNumerocuenta() {
        return numeroCuenta;
    }

    public void setNumerocuenta(String numeroCuenta) {
        this.numeroCuenta = numeroCuenta;
    }


}