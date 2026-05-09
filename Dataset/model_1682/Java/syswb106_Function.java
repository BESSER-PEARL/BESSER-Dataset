





import java.util.List;
import java.util.ArrayList;

public class syswb106_Function  {






    private List<syswb106_FunctionProperty> syswb106_functionpropertys;




    private syswb106_PatternCatalog syswb106_patterncatalog;




    private syswb106_System syswb106_system;




    private syswb106_Function syswb106_function;




    private syswb106_Function syswb106_function;


    public syswb106_Function(
    ) {
        this.syswb106_functionpropertys = new ArrayList<>();
    }

    public syswb106_Function(
        ArrayList<syswb106_FunctionProperty> syswb106_functionpropertys    ) {
        this.syswb106_functionpropertys = syswb106_functionpropertys;
    }


    public List<syswb106_FunctionProperty> getSyswb106_functionpropertys() {
        return syswb106_functionpropertys;
    }

    public void addSyswb106_functionproperty(Syswb106_functionproperty syswb106_functionproperty) {
        this.syswb106_functionpropertys.add(syswb106_functionproperty);
    }
    public syswb106_PatternCatalog getSyswb106_patterncatalog() {
        return syswb106_patterncatalog;
    }

    public void setSyswb106_patterncatalog(syswb106_PatternCatalog syswb106_patterncatalog) {
        this.syswb106_patterncatalog = syswb106_patterncatalog;
    }
    public syswb106_System getSyswb106_system() {
        return syswb106_system;
    }

    public void setSyswb106_system(syswb106_System syswb106_system) {
        this.syswb106_system = syswb106_system;
    }
    public syswb106_Function getSyswb106_function() {
        return syswb106_function;
    }

    public void setSyswb106_function(syswb106_Function syswb106_function) {
        this.syswb106_function = syswb106_function;
    }
    public syswb106_Function getSyswb106_function() {
        return syswb106_function;
    }

    public void setSyswb106_function(syswb106_Function syswb106_function) {
        this.syswb106_function = syswb106_function;
    }

}