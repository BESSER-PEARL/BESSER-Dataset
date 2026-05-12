





import java.util.List;
import java.util.ArrayList;

public class Fabricacion  {

    private String PteEquipoDirectivo;
    private int NroTrabajadoresBase;
    private String razonSocial;
    private String EquipoDirectivo;
    private int codigo;



    public Fabricacion(
        String PteEquipoDirectivo,        int NroTrabajadoresBase,        String razonSocial,        String EquipoDirectivo,        int codigo    ) {
        this.PteEquipoDirectivo = PteEquipoDirectivo;
        this.NroTrabajadoresBase = NroTrabajadoresBase;
        this.razonSocial = razonSocial;
        this.EquipoDirectivo = EquipoDirectivo;
        this.codigo = codigo;
    }


    public String getPteequipodirectivo() {
        return PteEquipoDirectivo;
    }

    public void setPteequipodirectivo(String PteEquipoDirectivo) {
        this.PteEquipoDirectivo = PteEquipoDirectivo;
    }
    public int getNrotrabajadoresbase() {
        return NroTrabajadoresBase;
    }

    public void setNrotrabajadoresbase(int NroTrabajadoresBase) {
        this.NroTrabajadoresBase = NroTrabajadoresBase;
    }
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getEquipodirectivo() {
        return EquipoDirectivo;
    }

    public void setEquipodirectivo(String EquipoDirectivo) {
        this.EquipoDirectivo = EquipoDirectivo;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }


}