





import java.util.List;
import java.util.ArrayList;

public class qvtimperativecs_MappingCallCS extends MappingStatementCS {

    private boolean isInfinite;





    private List<qvtimperativecs_MappingCallBindingCS> qvtimperativecs_mappingcallbindingcss;




    private qvtimperativecs_MappingCallBindingCS qvtimperativecs_mappingcallbindingcs;


    public qvtimperativecs_MappingCallCS(
        boolean isInfinite    ) {
        super(
        );
        this.isInfinite = isInfinite;
        this.qvtimperativecs_mappingcallbindingcss = new ArrayList<>();
    }

    public qvtimperativecs_MappingCallCS(
        boolean isInfinite        ArrayList<qvtimperativecs_MappingCallBindingCS> qvtimperativecs_mappingcallbindingcss    ) {
        this.isInfinite = isInfinite;
        this.qvtimperativecs_mappingcallbindingcss = qvtimperativecs_mappingcallbindingcss;
    }

    public boolean getIsinfinite() {
        return isInfinite;
    }

    public void setIsinfinite(boolean isInfinite) {
        this.isInfinite = isInfinite;
    }

    public List<qvtimperativecs_MappingCallBindingCS> getQvtimperativecs_mappingcallbindingcss() {
        return qvtimperativecs_mappingcallbindingcss;
    }

    public void addQvtimperativecs_mappingcallbindingcs(Qvtimperativecs_mappingcallbindingcs qvtimperativecs_mappingcallbindingcs) {
        this.qvtimperativecs_mappingcallbindingcss.add(qvtimperativecs_mappingcallbindingcs);
    }
    public qvtimperativecs_MappingCallBindingCS getQvtimperativecs_mappingcallbindingcs() {
        return qvtimperativecs_mappingcallbindingcs;
    }

    public void setQvtimperativecs_mappingcallbindingcs(qvtimperativecs_MappingCallBindingCS qvtimperativecs_mappingcallbindingcs) {
        this.qvtimperativecs_mappingcallbindingcs = qvtimperativecs_mappingcallbindingcs;
    }

}