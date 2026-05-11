





import java.util.List;
import java.util.ArrayList;

public class form_Group extends Duplicable, Widget {

    private boolean useIterator;
    private boolean showBorder;





    private List<form_Widget> form_widgets;




    private List<form_Line> form_lines;




    private List<form_Column> form_columns;




    private form_GroupIterator form_groupiterator;


    public form_Group(
        boolean useIterator,        boolean showBorder    ) {
        super(
        );
        this.useIterator = useIterator;
        this.showBorder = showBorder;
        this.form_widgets = new ArrayList<>();
        this.form_lines = new ArrayList<>();
        this.form_columns = new ArrayList<>();
    }

    public form_Group(
        boolean useIterator,        boolean showBorder        ArrayList<form_Widget> form_widgets,        ArrayList<form_Line> form_lines,        ArrayList<form_Column> form_columns    ) {
        this.useIterator = useIterator;
        this.showBorder = showBorder;
        this.form_widgets = form_widgets;
        this.form_lines = form_lines;
        this.form_columns = form_columns;
    }

    public boolean getUseiterator() {
        return useIterator;
    }

    public void setUseiterator(boolean useIterator) {
        this.useIterator = useIterator;
    }
    public boolean getShowborder() {
        return showBorder;
    }

    public void setShowborder(boolean showBorder) {
        this.showBorder = showBorder;
    }

    public List<form_Widget> getForm_widgets() {
        return form_widgets;
    }

    public void addForm_widget(Form_widget form_widget) {
        this.form_widgets.add(form_widget);
    }
    public List<form_Line> getForm_lines() {
        return form_lines;
    }

    public void addForm_line(Form_line form_line) {
        this.form_lines.add(form_line);
    }
    public List<form_Column> getForm_columns() {
        return form_columns;
    }

    public void addForm_column(Form_column form_column) {
        this.form_columns.add(form_column);
    }
    public form_GroupIterator getForm_groupiterator() {
        return form_groupiterator;
    }

    public void setForm_groupiterator(form_GroupIterator form_groupiterator) {
        this.form_groupiterator = form_groupiterator;
    }

}