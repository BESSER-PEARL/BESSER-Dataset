





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Function extends ProcessNode, SequenceNode {

    private String domain;





    private List<syswbeff1065ok_InputPort> syswbeff1065ok_inputports;




    private List<syswbeff1065ok_Description> syswbeff1065ok_descriptions;




    private syswbeff1065ok_Function syswbeff1065ok_function;




    private List<syswbeff1065ok_Token> syswbeff1065ok_tokens;




    private List<syswbeff1065ok_Function> syswbeff1065ok_functions;


    public syswbeff1065ok_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.syswbeff1065ok_inputports = new ArrayList<>();
        this.syswbeff1065ok_descriptions = new ArrayList<>();
        this.syswbeff1065ok_tokens = new ArrayList<>();
        this.syswbeff1065ok_functions = new ArrayList<>();
    }

    public syswbeff1065ok_Function(
        String domain        ArrayList<syswbeff1065ok_InputPort> syswbeff1065ok_inputports,        ArrayList<syswbeff1065ok_Description> syswbeff1065ok_descriptions,        ArrayList<syswbeff1065ok_Token> syswbeff1065ok_tokens,        ArrayList<syswbeff1065ok_Function> syswbeff1065ok_functions    ) {
        this.domain = domain;
        this.syswbeff1065ok_inputports = syswbeff1065ok_inputports;
        this.syswbeff1065ok_descriptions = syswbeff1065ok_descriptions;
        this.syswbeff1065ok_tokens = syswbeff1065ok_tokens;
        this.syswbeff1065ok_functions = syswbeff1065ok_functions;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<syswbeff1065ok_InputPort> getSyswbeff1065ok_inputports() {
        return syswbeff1065ok_inputports;
    }

    public void addSyswbeff1065ok_inputport(Syswbeff1065ok_inputport syswbeff1065ok_inputport) {
        this.syswbeff1065ok_inputports.add(syswbeff1065ok_inputport);
    }
    public List<syswbeff1065ok_Description> getSyswbeff1065ok_descriptions() {
        return syswbeff1065ok_descriptions;
    }

    public void addSyswbeff1065ok_description(Syswbeff1065ok_description syswbeff1065ok_description) {
        this.syswbeff1065ok_descriptions.add(syswbeff1065ok_description);
    }
    public syswbeff1065ok_Function getSyswbeff1065ok_function() {
        return syswbeff1065ok_function;
    }

    public void setSyswbeff1065ok_function(syswbeff1065ok_Function syswbeff1065ok_function) {
        this.syswbeff1065ok_function = syswbeff1065ok_function;
    }
    public List<syswbeff1065ok_Token> getSyswbeff1065ok_tokens() {
        return syswbeff1065ok_tokens;
    }

    public void addSyswbeff1065ok_token(Syswbeff1065ok_token syswbeff1065ok_token) {
        this.syswbeff1065ok_tokens.add(syswbeff1065ok_token);
    }
    public List<syswbeff1065ok_Function> getSyswbeff1065ok_functions() {
        return syswbeff1065ok_functions;
    }

    public void addSyswbeff1065ok_function(Syswbeff1065ok_function syswbeff1065ok_function) {
        this.syswbeff1065ok_functions.add(syswbeff1065ok_function);
    }

}