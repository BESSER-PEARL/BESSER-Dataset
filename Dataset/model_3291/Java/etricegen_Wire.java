





import java.util.List;
import java.util.ArrayList;

public class etricegen_Wire  {

    private String path1;
    private String path2;
    private boolean dataDriven;





    private etricegen_WiredStructureClass etricegen_wiredstructureclass;


    public etricegen_Wire(
        String path1,        String path2,        boolean dataDriven    ) {
        this.path1 = path1;
        this.path2 = path2;
        this.dataDriven = dataDriven;
    }


    public String getPath1() {
        return path1;
    }

    public void setPath1(String path1) {
        this.path1 = path1;
    }
    public String getPath2() {
        return path2;
    }

    public void setPath2(String path2) {
        this.path2 = path2;
    }
    public boolean getDatadriven() {
        return dataDriven;
    }

    public void setDatadriven(boolean dataDriven) {
        this.dataDriven = dataDriven;
    }

    public etricegen_WiredStructureClass getEtricegen_wiredstructureclass() {
        return etricegen_wiredstructureclass;
    }

    public void setEtricegen_wiredstructureclass(etricegen_WiredStructureClass etricegen_wiredstructureclass) {
        this.etricegen_wiredstructureclass = etricegen_wiredstructureclass;
    }

}