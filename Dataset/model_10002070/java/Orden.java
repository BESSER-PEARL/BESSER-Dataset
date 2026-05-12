





import java.util.List;
import java.util.ArrayList;

public class Orden  {

    private boolean pagada;
    private int mesa;
    private boolean preparada;
    private String fecha;
    private String orden_Id;
    private int numComensales;
    private boolean servida;



    public Orden(
        boolean pagada,        int mesa,        boolean preparada,        String fecha,        String orden_Id,        int numComensales,        boolean servida    ) {
        this.pagada = pagada;
        this.mesa = mesa;
        this.preparada = preparada;
        this.fecha = fecha;
        this.orden_Id = orden_Id;
        this.numComensales = numComensales;
        this.servida = servida;
    }


    public boolean getPagada() {
        return pagada;
    }

    public void setPagada(boolean pagada) {
        this.pagada = pagada;
    }
    public int getMesa() {
        return mesa;
    }

    public void setMesa(int mesa) {
        this.mesa = mesa;
    }
    public boolean getPreparada() {
        return preparada;
    }

    public void setPreparada(boolean preparada) {
        this.preparada = preparada;
    }
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }
    public String getOrden_id() {
        return orden_Id;
    }

    public void setOrden_id(String orden_Id) {
        this.orden_Id = orden_Id;
    }
    public int getNumcomensales() {
        return numComensales;
    }

    public void setNumcomensales(int numComensales) {
        this.numComensales = numComensales;
    }
    public boolean getServida() {
        return servida;
    }

    public void setServida(boolean servida) {
        this.servida = servida;
    }


}