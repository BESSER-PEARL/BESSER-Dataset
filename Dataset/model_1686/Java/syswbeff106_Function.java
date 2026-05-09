





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_Function extends ProcessNode, SequenceNode {

    private String domain;





    private List<syswbeff106_Function> syswbeff106_functions;




    private syswbeff106_Function syswbeff106_function;


    public syswbeff106_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.syswbeff106_functions = new ArrayList<>();
    }

    public syswbeff106_Function(
        String domain        ArrayList<syswbeff106_Function> syswbeff106_functions    ) {
        this.domain = domain;
        this.syswbeff106_functions = syswbeff106_functions;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<syswbeff106_Function> getSyswbeff106_functions() {
        return syswbeff106_functions;
    }

    public void addSyswbeff106_function(Syswbeff106_function syswbeff106_function) {
        this.syswbeff106_functions.add(syswbeff106_function);
    }
    public syswbeff106_Function getSyswbeff106_function() {
        return syswbeff106_function;
    }

    public void setSyswbeff106_function(syswbeff106_Function syswbeff106_function) {
        this.syswbeff106_function = syswbeff106_function;
    }

}