





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Workbench  {






    private List<syswbeff1065ok_PatternCatalog> syswbeff1065ok_patterncatalogs;




    private List<syswbeff1065ok_FunctionProperty> syswbeff1065ok_functionpropertys;




    private List<syswbeff1065ok_Thing> syswbeff1065ok_things;




    private syswbeff1065ok_System syswbeff1065ok_system;




    private List<syswbeff1065ok_Thoughts> syswbeff1065ok_thoughtss;


    public syswbeff1065ok_Workbench(
    ) {
        this.syswbeff1065ok_patterncatalogs = new ArrayList<>();
        this.syswbeff1065ok_functionpropertys = new ArrayList<>();
        this.syswbeff1065ok_things = new ArrayList<>();
        this.syswbeff1065ok_thoughtss = new ArrayList<>();
    }

    public syswbeff1065ok_Workbench(
        ArrayList<syswbeff1065ok_PatternCatalog> syswbeff1065ok_patterncatalogs,        ArrayList<syswbeff1065ok_FunctionProperty> syswbeff1065ok_functionpropertys,        ArrayList<syswbeff1065ok_Thing> syswbeff1065ok_things,        ArrayList<syswbeff1065ok_Thoughts> syswbeff1065ok_thoughtss    ) {
        this.syswbeff1065ok_patterncatalogs = syswbeff1065ok_patterncatalogs;
        this.syswbeff1065ok_functionpropertys = syswbeff1065ok_functionpropertys;
        this.syswbeff1065ok_things = syswbeff1065ok_things;
        this.syswbeff1065ok_thoughtss = syswbeff1065ok_thoughtss;
    }


    public List<syswbeff1065ok_PatternCatalog> getSyswbeff1065ok_patterncatalogs() {
        return syswbeff1065ok_patterncatalogs;
    }

    public void addSyswbeff1065ok_patterncatalog(Syswbeff1065ok_patterncatalog syswbeff1065ok_patterncatalog) {
        this.syswbeff1065ok_patterncatalogs.add(syswbeff1065ok_patterncatalog);
    }
    public List<syswbeff1065ok_FunctionProperty> getSyswbeff1065ok_functionpropertys() {
        return syswbeff1065ok_functionpropertys;
    }

    public void addSyswbeff1065ok_functionproperty(Syswbeff1065ok_functionproperty syswbeff1065ok_functionproperty) {
        this.syswbeff1065ok_functionpropertys.add(syswbeff1065ok_functionproperty);
    }
    public List<syswbeff1065ok_Thing> getSyswbeff1065ok_things() {
        return syswbeff1065ok_things;
    }

    public void addSyswbeff1065ok_thing(Syswbeff1065ok_thing syswbeff1065ok_thing) {
        this.syswbeff1065ok_things.add(syswbeff1065ok_thing);
    }
    public syswbeff1065ok_System getSyswbeff1065ok_system() {
        return syswbeff1065ok_system;
    }

    public void setSyswbeff1065ok_system(syswbeff1065ok_System syswbeff1065ok_system) {
        this.syswbeff1065ok_system = syswbeff1065ok_system;
    }
    public List<syswbeff1065ok_Thoughts> getSyswbeff1065ok_thoughtss() {
        return syswbeff1065ok_thoughtss;
    }

    public void addSyswbeff1065ok_thoughts(Syswbeff1065ok_thoughts syswbeff1065ok_thoughts) {
        this.syswbeff1065ok_thoughtss.add(syswbeff1065ok_thoughts);
    }

}