





import java.util.List;
import java.util.ArrayList;

public class table_DTableElementStyle  {

    private String labelFormat;
    private int labelSize;
    private boolean defaultForegroundStyle;
    private boolean defaultBackgroundStyle;





    private table_DColumn table_dcolumn;




    private table_DLine table_dline;


    public table_DTableElementStyle(
        String labelFormat,        int labelSize,        boolean defaultForegroundStyle,        boolean defaultBackgroundStyle    ) {
        this.labelFormat = labelFormat;
        this.labelSize = labelSize;
        this.defaultForegroundStyle = defaultForegroundStyle;
        this.defaultBackgroundStyle = defaultBackgroundStyle;
    }


    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }
    public boolean getDefaultforegroundstyle() {
        return defaultForegroundStyle;
    }

    public void setDefaultforegroundstyle(boolean defaultForegroundStyle) {
        this.defaultForegroundStyle = defaultForegroundStyle;
    }
    public boolean getDefaultbackgroundstyle() {
        return defaultBackgroundStyle;
    }

    public void setDefaultbackgroundstyle(boolean defaultBackgroundStyle) {
        this.defaultBackgroundStyle = defaultBackgroundStyle;
    }

    public table_DColumn getTable_dcolumn() {
        return table_dcolumn;
    }

    public void setTable_dcolumn(table_DColumn table_dcolumn) {
        this.table_dcolumn = table_dcolumn;
    }
    public table_DLine getTable_dline() {
        return table_dline;
    }

    public void setTable_dline(table_DLine table_dline) {
        this.table_dline = table_dline;
    }

}