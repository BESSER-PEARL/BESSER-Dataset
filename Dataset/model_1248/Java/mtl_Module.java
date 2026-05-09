





import java.util.List;
import java.util.ArrayList;

public class mtl_Module extends EPackage, DocumentedElement {

    private int startHeaderPosition;
    private int endHeaderPosition;





    private mtl_Module mtl_module;




    private List<mtl_Module> mtl_modules;


    public mtl_Module(
        int startHeaderPosition,        int endHeaderPosition    ) {
        super(
        );
        this.startHeaderPosition = startHeaderPosition;
        this.endHeaderPosition = endHeaderPosition;
        this.mtl_modules = new ArrayList<>();
    }

    public mtl_Module(
        int startHeaderPosition,        int endHeaderPosition        ArrayList<mtl_Module> mtl_modules    ) {
        this.startHeaderPosition = startHeaderPosition;
        this.endHeaderPosition = endHeaderPosition;
        this.mtl_modules = mtl_modules;
    }

    public int getStartheaderposition() {
        return startHeaderPosition;
    }

    public void setStartheaderposition(int startHeaderPosition) {
        this.startHeaderPosition = startHeaderPosition;
    }
    public int getEndheaderposition() {
        return endHeaderPosition;
    }

    public void setEndheaderposition(int endHeaderPosition) {
        this.endHeaderPosition = endHeaderPosition;
    }

    public mtl_Module getMtl_module() {
        return mtl_module;
    }

    public void setMtl_module(mtl_Module mtl_module) {
        this.mtl_module = mtl_module;
    }
    public List<mtl_Module> getMtl_modules() {
        return mtl_modules;
    }

    public void addMtl_module(Mtl_module mtl_module) {
        this.mtl_modules.add(mtl_module);
    }

}