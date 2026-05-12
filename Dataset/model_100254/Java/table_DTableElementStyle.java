





import java.util.List;
import java.util.ArrayList;

public class table_DTableElementStyle  {

    private boolean defaultBackgroundStyle;
    private String labelFormat;
    private boolean defaultForegroundStyle;
    private int labelSize;





    private table_DLine table_dline;




    private table_DColumn table_dcolumn;


    public table_DTableElementStyle(
        boolean defaultBackgroundStyle,        String labelFormat,        boolean defaultForegroundStyle,        int labelSize    ) {
        this.defaultBackgroundStyle = defaultBackgroundStyle;
        this.labelFormat = labelFormat;
        this.defaultForegroundStyle = defaultForegroundStyle;
        this.labelSize = labelSize;
    }


    public boolean getDefaultbackgroundstyle() {
        return defaultBackgroundStyle;
    }

    public void setDefaultbackgroundstyle(boolean defaultBackgroundStyle) {
        this.defaultBackgroundStyle = defaultBackgroundStyle;
    }
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public boolean getDefaultforegroundstyle() {
        return defaultForegroundStyle;
    }

    public void setDefaultforegroundstyle(boolean defaultForegroundStyle) {
        this.defaultForegroundStyle = defaultForegroundStyle;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }

    public table_DLine getTable_dline() {
        return table_dline;
    }

    public void setTable_dline(table_DLine table_dline) {
        this.table_dline = table_dline;
    }
    public table_DColumn getTable_dcolumn() {
        return table_dcolumn;
    }

    public void setTable_dcolumn(table_DColumn table_dcolumn) {
        this.table_dcolumn = table_dcolumn;
    }

}