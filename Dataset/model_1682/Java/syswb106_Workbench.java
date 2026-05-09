





import java.util.List;
import java.util.ArrayList;

public class syswb106_Workbench  {

    private String aprop;





    private List<syswb106_Thoughts> syswb106_thoughtss;




    private List<syswb106_PatternCatalog> syswb106_patterncatalogs;




    private List<syswb106_FunctionProperty> syswb106_functionpropertys;




    private syswb106_System syswb106_system;


    public syswb106_Workbench(
        String aprop    ) {
        this.aprop = aprop;
        this.syswb106_thoughtss = new ArrayList<>();
        this.syswb106_patterncatalogs = new ArrayList<>();
        this.syswb106_functionpropertys = new ArrayList<>();
    }

    public syswb106_Workbench(
        String aprop        ArrayList<syswb106_Thoughts> syswb106_thoughtss,        ArrayList<syswb106_PatternCatalog> syswb106_patterncatalogs,        ArrayList<syswb106_FunctionProperty> syswb106_functionpropertys    ) {
        this.aprop = aprop;
        this.syswb106_thoughtss = syswb106_thoughtss;
        this.syswb106_patterncatalogs = syswb106_patterncatalogs;
        this.syswb106_functionpropertys = syswb106_functionpropertys;
    }

    public String getAprop() {
        return aprop;
    }

    public void setAprop(String aprop) {
        this.aprop = aprop;
    }

    public List<syswb106_Thoughts> getSyswb106_thoughtss() {
        return syswb106_thoughtss;
    }

    public void addSyswb106_thoughts(Syswb106_thoughts syswb106_thoughts) {
        this.syswb106_thoughtss.add(syswb106_thoughts);
    }
    public List<syswb106_PatternCatalog> getSyswb106_patterncatalogs() {
        return syswb106_patterncatalogs;
    }

    public void addSyswb106_patterncatalog(Syswb106_patterncatalog syswb106_patterncatalog) {
        this.syswb106_patterncatalogs.add(syswb106_patterncatalog);
    }
    public List<syswb106_FunctionProperty> getSyswb106_functionpropertys() {
        return syswb106_functionpropertys;
    }

    public void addSyswb106_functionproperty(Syswb106_functionproperty syswb106_functionproperty) {
        this.syswb106_functionpropertys.add(syswb106_functionproperty);
    }
    public syswb106_System getSyswb106_system() {
        return syswb106_system;
    }

    public void setSyswb106_system(syswb106_System syswb106_system) {
        this.syswb106_system = syswb106_system;
    }

}