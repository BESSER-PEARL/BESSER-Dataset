





import java.util.List;
import java.util.ArrayList;

public class java_Try_statement  {

    private String finally_;
    private String catchs;
    private String try_;





    private java_Statement java_statement;




    private List<java_Parameter> java_parameters;




    private java_Statement java_statement;




    private List<java_Statement> java_statements;




    private java_Statement java_statement;


    public java_Try_statement(
        String finally_,        String catchs,        String try_    ) {
        this.finally_ = finally_;
        this.catchs = catchs;
        this.try_ = try_;
        this.java_parameters = new ArrayList<>();
        this.java_statements = new ArrayList<>();
    }

    public java_Try_statement(
        String finally_,        String catchs,        String try_        ArrayList<java_Parameter> java_parameters,        ArrayList<java_Statement> java_statements    ) {
        this.finally_ = finally_;
        this.catchs = catchs;
        this.try_ = try_;
        this.java_parameters = java_parameters;
        this.java_statements = java_statements;
    }

    public String getFinally_() {
        return finally_;
    }

    public void setFinally_(String finally_) {
        this.finally_ = finally_;
    }
    public String getCatchs() {
        return catchs;
    }

    public void setCatchs(String catchs) {
        this.catchs = catchs;
    }
    public String getTry_() {
        return try_;
    }

    public void setTry_(String try_) {
        this.try_ = try_;
    }

    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }
    public List<java_Parameter> getJava_parameters() {
        return java_parameters;
    }

    public void addJava_parameter(Java_parameter java_parameter) {
        this.java_parameters.add(java_parameter);
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }
    public List<java_Statement> getJava_statements() {
        return java_statements;
    }

    public void addJava_statement(Java_statement java_statement) {
        this.java_statements.add(java_statement);
    }
    public java_Statement getJava_statement() {
        return java_statement;
    }

    public void setJava_statement(java_Statement java_statement) {
        this.java_statement = java_statement;
    }

}