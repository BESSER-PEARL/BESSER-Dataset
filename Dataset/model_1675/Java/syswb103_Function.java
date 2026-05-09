





import java.util.List;
import java.util.ArrayList;

public class syswb103_Function extends NamedElement {






    private syswb103_System syswb103_system;




    private List<syswb103_Function> syswb103_functions;




    private List<syswb103_FunctionProperty> syswb103_functionpropertys;




    private syswb103_PatternCatalog syswb103_patterncatalog;




    private syswb103_Function syswb103_function;


    public syswb103_Function(
    ) {
        super(
        );
        this.syswb103_functions = new ArrayList<>();
        this.syswb103_functionpropertys = new ArrayList<>();
    }

    public syswb103_Function(
        ArrayList<syswb103_Function> syswb103_functions,        ArrayList<syswb103_FunctionProperty> syswb103_functionpropertys    ) {
        this.syswb103_functions = syswb103_functions;
        this.syswb103_functionpropertys = syswb103_functionpropertys;
    }


    public syswb103_System getSyswb103_system() {
        return syswb103_system;
    }

    public void setSyswb103_system(syswb103_System syswb103_system) {
        this.syswb103_system = syswb103_system;
    }
    public List<syswb103_Function> getSyswb103_functions() {
        return syswb103_functions;
    }

    public void addSyswb103_function(Syswb103_function syswb103_function) {
        this.syswb103_functions.add(syswb103_function);
    }
    public List<syswb103_FunctionProperty> getSyswb103_functionpropertys() {
        return syswb103_functionpropertys;
    }

    public void addSyswb103_functionproperty(Syswb103_functionproperty syswb103_functionproperty) {
        this.syswb103_functionpropertys.add(syswb103_functionproperty);
    }
    public syswb103_PatternCatalog getSyswb103_patterncatalog() {
        return syswb103_patterncatalog;
    }

    public void setSyswb103_patterncatalog(syswb103_PatternCatalog syswb103_patterncatalog) {
        this.syswb103_patterncatalog = syswb103_patterncatalog;
    }
    public syswb103_Function getSyswb103_function() {
        return syswb103_function;
    }

    public void setSyswb103_function(syswb103_Function syswb103_function) {
        this.syswb103_function = syswb103_function;
    }

}