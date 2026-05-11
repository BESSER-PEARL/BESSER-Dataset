





import java.util.List;
import java.util.ArrayList;

public class b_Operation  {

    private String name;





    private List<b_Variable> b_variables;




    private b_Body b_body;




    private b_LocalOperations b_localoperations;




    private b_Call b_call;




    private b_Operations b_operations;




    private List<b_Variable> b_variables;


    public b_Operation(
        String name    ) {
        this.name = name;
        this.b_variables = new ArrayList<>();
        this.b_variables = new ArrayList<>();
    }

    public b_Operation(
        String name        ArrayList<b_Variable> b_variables,        ArrayList<b_Variable> b_variables    ) {
        this.name = name;
        this.b_variables = b_variables;
        this.b_variables = b_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }
    public b_Body getB_body() {
        return b_body;
    }

    public void setB_body(b_Body b_body) {
        this.b_body = b_body;
    }
    public b_LocalOperations getB_localoperations() {
        return b_localoperations;
    }

    public void setB_localoperations(b_LocalOperations b_localoperations) {
        this.b_localoperations = b_localoperations;
    }
    public b_Call getB_call() {
        return b_call;
    }

    public void setB_call(b_Call b_call) {
        this.b_call = b_call;
    }
    public b_Operations getB_operations() {
        return b_operations;
    }

    public void setB_operations(b_Operations b_operations) {
        this.b_operations = b_operations;
    }
    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }

}