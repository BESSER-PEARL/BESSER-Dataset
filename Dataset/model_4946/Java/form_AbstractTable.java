





import java.util.List;
import java.util.ArrayList;

public class form_AbstractTable extends Duplicable, Widget {

    private boolean useVerticalHeader;
    private boolean LastRowIsHeader;
    private boolean firstRowIsHeader;
    private boolean rightColumnIsHeader;
    private boolean useHorizontalHeader;
    private boolean initializedUsingCells;
    private boolean leftColumnIsHeader;





    private form_Expression form_expression;




    private form_Expression form_expression;


    public form_AbstractTable(
        boolean useVerticalHeader,        boolean LastRowIsHeader,        boolean firstRowIsHeader,        boolean rightColumnIsHeader,        boolean useHorizontalHeader,        boolean initializedUsingCells,        boolean leftColumnIsHeader    ) {
        super(
        );
        this.useVerticalHeader = useVerticalHeader;
        this.LastRowIsHeader = LastRowIsHeader;
        this.firstRowIsHeader = firstRowIsHeader;
        this.rightColumnIsHeader = rightColumnIsHeader;
        this.useHorizontalHeader = useHorizontalHeader;
        this.initializedUsingCells = initializedUsingCells;
        this.leftColumnIsHeader = leftColumnIsHeader;
    }


    public boolean getUseverticalheader() {
        return useVerticalHeader;
    }

    public void setUseverticalheader(boolean useVerticalHeader) {
        this.useVerticalHeader = useVerticalHeader;
    }
    public boolean getLastrowisheader() {
        return LastRowIsHeader;
    }

    public void setLastrowisheader(boolean LastRowIsHeader) {
        this.LastRowIsHeader = LastRowIsHeader;
    }
    public boolean getFirstrowisheader() {
        return firstRowIsHeader;
    }

    public void setFirstrowisheader(boolean firstRowIsHeader) {
        this.firstRowIsHeader = firstRowIsHeader;
    }
    public boolean getRightcolumnisheader() {
        return rightColumnIsHeader;
    }

    public void setRightcolumnisheader(boolean rightColumnIsHeader) {
        this.rightColumnIsHeader = rightColumnIsHeader;
    }
    public boolean getUsehorizontalheader() {
        return useHorizontalHeader;
    }

    public void setUsehorizontalheader(boolean useHorizontalHeader) {
        this.useHorizontalHeader = useHorizontalHeader;
    }
    public boolean getInitializedusingcells() {
        return initializedUsingCells;
    }

    public void setInitializedusingcells(boolean initializedUsingCells) {
        this.initializedUsingCells = initializedUsingCells;
    }
    public boolean getLeftcolumnisheader() {
        return leftColumnIsHeader;
    }

    public void setLeftcolumnisheader(boolean leftColumnIsHeader) {
        this.leftColumnIsHeader = leftColumnIsHeader;
    }

    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }
    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}