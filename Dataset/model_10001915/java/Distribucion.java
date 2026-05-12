





import java.util.List;
import java.util.ArrayList;

public class Distribucion  {

    private int NroTrabajadoresBase;
    private int codigo;
    private String PteEquipoDirectivo;
    private String EquipoDirectivo;
    private String razonSocial;



    public Distribucion(
        int NroTrabajadoresBase,        int codigo,        String PteEquipoDirectivo,        String EquipoDirectivo,        String razonSocial    ) {
        this.NroTrabajadoresBase = NroTrabajadoresBase;
        this.codigo = codigo;
        this.PteEquipoDirectivo = PteEquipoDirectivo;
        this.EquipoDirectivo = EquipoDirectivo;
        this.razonSocial = razonSocial;
    }


    public int getNrotrabajadoresbase() {
        return NroTrabajadoresBase;
    }

    public void setNrotrabajadoresbase(int NroTrabajadoresBase) {
        this.NroTrabajadoresBase = NroTrabajadoresBase;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getPteequipodirectivo() {
        return PteEquipoDirectivo;
    }

    public void setPteequipodirectivo(String PteEquipoDirectivo) {
        this.PteEquipoDirectivo = PteEquipoDirectivo;
    }
    public String getEquipodirectivo() {
        return EquipoDirectivo;
    }

    public void setEquipodirectivo(String EquipoDirectivo) {
        this.EquipoDirectivo = EquipoDirectivo;
    }
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }


}