





import java.util.List;
import java.util.ArrayList;

public class facturas_pagos_  {

    private String codigo;
    private String total;
    private int pagoNomina;





    private Obras obras;




    private List<Trabajadores> trabajadoress;


    public facturas_pagos_(
        String codigo,        String total,        int pagoNomina    ) {
        this.codigo = codigo;
        this.total = total;
        this.pagoNomina = pagoNomina;
        this.trabajadoress = new ArrayList<>();
    }

    public facturas_pagos_(
        String codigo,        String total,        int pagoNomina        ArrayList<Trabajadores> trabajadoress    ) {
        this.codigo = codigo;
        this.total = total;
        this.pagoNomina = pagoNomina;
        this.trabajadoress = trabajadoress;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public int getPagonomina() {
        return pagoNomina;
    }

    public void setPagonomina(int pagoNomina) {
        this.pagoNomina = pagoNomina;
    }

    public Obras getObras() {
        return obras;
    }

    public void setObras(Obras obras) {
        this.obras = obras;
    }
    public List<Trabajadores> getTrabajadoress() {
        return trabajadoress;
    }

    public void addTrabajadores(Trabajadores trabajadores) {
        this.trabajadoress.add(trabajadores);
    }

}