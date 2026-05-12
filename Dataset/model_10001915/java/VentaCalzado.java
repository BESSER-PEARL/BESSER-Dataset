





import java.util.List;
import java.util.ArrayList;

public class VentaCalzado  {

    private String razonSocial;
    private String EquipoDirectivo;
    private int NroTrabajadoresBase;
    private String PteEquipoDirectivo;
    private int codigo;



    public VentaCalzado(
        String razonSocial,        String EquipoDirectivo,        int NroTrabajadoresBase,        String PteEquipoDirectivo,        int codigo    ) {
        this.razonSocial = razonSocial;
        this.EquipoDirectivo = EquipoDirectivo;
        this.NroTrabajadoresBase = NroTrabajadoresBase;
        this.PteEquipoDirectivo = PteEquipoDirectivo;
        this.codigo = codigo;
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
    public int getNrotrabajadoresbase() {
        return NroTrabajadoresBase;
    }

    public void setNrotrabajadoresbase(int NroTrabajadoresBase) {
        this.NroTrabajadoresBase = NroTrabajadoresBase;
    }
    public String getPteequipodirectivo() {
        return PteEquipoDirectivo;
    }

    public void setPteequipodirectivo(String PteEquipoDirectivo) {
        this.PteEquipoDirectivo = PteEquipoDirectivo;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }


}