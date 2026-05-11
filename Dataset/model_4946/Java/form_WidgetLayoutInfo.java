





import java.util.List;
import java.util.ArrayList;

public class form_WidgetLayoutInfo  {

    private int horizontalSpan;
    private int verticalSpan;
    private int column;
    private int line;





    private form_Widget form_widget;


    public form_WidgetLayoutInfo(
        int horizontalSpan,        int verticalSpan,        int column,        int line    ) {
        this.horizontalSpan = horizontalSpan;
        this.verticalSpan = verticalSpan;
        this.column = column;
        this.line = line;
    }


    public int getHorizontalspan() {
        return horizontalSpan;
    }

    public void setHorizontalspan(int horizontalSpan) {
        this.horizontalSpan = horizontalSpan;
    }
    public int getVerticalspan() {
        return verticalSpan;
    }

    public void setVerticalspan(int verticalSpan) {
        this.verticalSpan = verticalSpan;
    }
    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }

    public form_Widget getForm_widget() {
        return form_widget;
    }

    public void setForm_widget(form_Widget form_widget) {
        this.form_widget = form_widget;
    }

}