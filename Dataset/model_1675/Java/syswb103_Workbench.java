





import java.util.List;
import java.util.ArrayList;

public class syswb103_Workbench extends NamedElement {

    private String aprop;





    private List<syswb103_PatternCatalog> syswb103_patterncatalogs;




    private syswb103_System syswb103_system;




    private List<syswb103_FunctionProperty> syswb103_functionpropertys;


    public syswb103_Workbench(
        String aprop    ) {
        super(
        );
        this.aprop = aprop;
        this.syswb103_patterncatalogs = new ArrayList<>();
        this.syswb103_functionpropertys = new ArrayList<>();
    }

    public syswb103_Workbench(
        String aprop        ArrayList<syswb103_PatternCatalog> syswb103_patterncatalogs,        ArrayList<syswb103_FunctionProperty> syswb103_functionpropertys    ) {
        this.aprop = aprop;
        this.syswb103_patterncatalogs = syswb103_patterncatalogs;
        this.syswb103_functionpropertys = syswb103_functionpropertys;
    }

    public String getAprop() {
        return aprop;
    }

    public void setAprop(String aprop) {
        this.aprop = aprop;
    }

    public List<syswb103_PatternCatalog> getSyswb103_patterncatalogs() {
        return syswb103_patterncatalogs;
    }

    public void addSyswb103_patterncatalog(Syswb103_patterncatalog syswb103_patterncatalog) {
        this.syswb103_patterncatalogs.add(syswb103_patterncatalog);
    }
    public syswb103_System getSyswb103_system() {
        return syswb103_system;
    }

    public void setSyswb103_system(syswb103_System syswb103_system) {
        this.syswb103_system = syswb103_system;
    }
    public List<syswb103_FunctionProperty> getSyswb103_functionpropertys() {
        return syswb103_functionpropertys;
    }

    public void addSyswb103_functionproperty(Syswb103_functionproperty syswb103_functionproperty) {
        this.syswb103_functionpropertys.add(syswb103_functionproperty);
    }

}