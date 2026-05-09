





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_Workbench  {

    private String aprop;





    private List<syswbeff106_PatternCatalog> syswbeff106_patterncatalogs;




    private List<syswbeff106_Thoughts> syswbeff106_thoughtss;




    private List<syswbeff106_Thing> syswbeff106_things;




    private List<syswbeff106_FunctionProperty> syswbeff106_functionpropertys;




    private syswbeff106_System syswbeff106_system;


    public syswbeff106_Workbench(
        String aprop    ) {
        this.aprop = aprop;
        this.syswbeff106_patterncatalogs = new ArrayList<>();
        this.syswbeff106_thoughtss = new ArrayList<>();
        this.syswbeff106_things = new ArrayList<>();
        this.syswbeff106_functionpropertys = new ArrayList<>();
    }

    public syswbeff106_Workbench(
        String aprop        ArrayList<syswbeff106_PatternCatalog> syswbeff106_patterncatalogs,        ArrayList<syswbeff106_Thoughts> syswbeff106_thoughtss,        ArrayList<syswbeff106_Thing> syswbeff106_things,        ArrayList<syswbeff106_FunctionProperty> syswbeff106_functionpropertys    ) {
        this.aprop = aprop;
        this.syswbeff106_patterncatalogs = syswbeff106_patterncatalogs;
        this.syswbeff106_thoughtss = syswbeff106_thoughtss;
        this.syswbeff106_things = syswbeff106_things;
        this.syswbeff106_functionpropertys = syswbeff106_functionpropertys;
    }

    public String getAprop() {
        return aprop;
    }

    public void setAprop(String aprop) {
        this.aprop = aprop;
    }

    public List<syswbeff106_PatternCatalog> getSyswbeff106_patterncatalogs() {
        return syswbeff106_patterncatalogs;
    }

    public void addSyswbeff106_patterncatalog(Syswbeff106_patterncatalog syswbeff106_patterncatalog) {
        this.syswbeff106_patterncatalogs.add(syswbeff106_patterncatalog);
    }
    public List<syswbeff106_Thoughts> getSyswbeff106_thoughtss() {
        return syswbeff106_thoughtss;
    }

    public void addSyswbeff106_thoughts(Syswbeff106_thoughts syswbeff106_thoughts) {
        this.syswbeff106_thoughtss.add(syswbeff106_thoughts);
    }
    public List<syswbeff106_Thing> getSyswbeff106_things() {
        return syswbeff106_things;
    }

    public void addSyswbeff106_thing(Syswbeff106_thing syswbeff106_thing) {
        this.syswbeff106_things.add(syswbeff106_thing);
    }
    public List<syswbeff106_FunctionProperty> getSyswbeff106_functionpropertys() {
        return syswbeff106_functionpropertys;
    }

    public void addSyswbeff106_functionproperty(Syswbeff106_functionproperty syswbeff106_functionproperty) {
        this.syswbeff106_functionpropertys.add(syswbeff106_functionproperty);
    }
    public syswbeff106_System getSyswbeff106_system() {
        return syswbeff106_system;
    }

    public void setSyswbeff106_system(syswbeff106_System syswbeff106_system) {
        this.syswbeff106_system = syswbeff106_system;
    }

}