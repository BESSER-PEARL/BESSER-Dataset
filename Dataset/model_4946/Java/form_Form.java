





import java.util.List;
import java.util.ArrayList;

public class form_Form extends ConnectableElement, Validable {

    private String version;
    private String showPageLabel;
    private int nColumn;
    private int nLine;
    private boolean allowHTMLInPageLabel;





    private List<form_Widget> form_widgets;




    private List<form_Operation> form_operations;




    private List<form_Line> form_lines;




    private form_Expression form_expression;




    private List<form_Column> form_columns;


    public form_Form(
        String version,        String showPageLabel,        int nColumn,        int nLine,        boolean allowHTMLInPageLabel    ) {
        super(
        );
        this.version = version;
        this.showPageLabel = showPageLabel;
        this.nColumn = nColumn;
        this.nLine = nLine;
        this.allowHTMLInPageLabel = allowHTMLInPageLabel;
        this.form_widgets = new ArrayList<>();
        this.form_operations = new ArrayList<>();
        this.form_lines = new ArrayList<>();
        this.form_columns = new ArrayList<>();
    }

    public form_Form(
        String version,        String showPageLabel,        int nColumn,        int nLine,        boolean allowHTMLInPageLabel        ArrayList<form_Widget> form_widgets,        ArrayList<form_Operation> form_operations,        ArrayList<form_Line> form_lines,        ArrayList<form_Column> form_columns    ) {
        this.version = version;
        this.showPageLabel = showPageLabel;
        this.nColumn = nColumn;
        this.nLine = nLine;
        this.allowHTMLInPageLabel = allowHTMLInPageLabel;
        this.form_widgets = form_widgets;
        this.form_operations = form_operations;
        this.form_lines = form_lines;
        this.form_columns = form_columns;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getShowpagelabel() {
        return showPageLabel;
    }

    public void setShowpagelabel(String showPageLabel) {
        this.showPageLabel = showPageLabel;
    }
    public int getNcolumn() {
        return nColumn;
    }

    public void setNcolumn(int nColumn) {
        this.nColumn = nColumn;
    }
    public int getNline() {
        return nLine;
    }

    public void setNline(int nLine) {
        this.nLine = nLine;
    }
    public boolean getAllowhtmlinpagelabel() {
        return allowHTMLInPageLabel;
    }

    public void setAllowhtmlinpagelabel(boolean allowHTMLInPageLabel) {
        this.allowHTMLInPageLabel = allowHTMLInPageLabel;
    }

    public List<form_Widget> getForm_widgets() {
        return form_widgets;
    }

    public void addForm_widget(Form_widget form_widget) {
        this.form_widgets.add(form_widget);
    }
    public List<form_Operation> getForm_operations() {
        return form_operations;
    }

    public void addForm_operation(Form_operation form_operation) {
        this.form_operations.add(form_operation);
    }
    public List<form_Line> getForm_lines() {
        return form_lines;
    }

    public void addForm_line(Form_line form_line) {
        this.form_lines.add(form_line);
    }
    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }
    public List<form_Column> getForm_columns() {
        return form_columns;
    }

    public void addForm_column(Form_column form_column) {
        this.form_columns.add(form_column);
    }

}