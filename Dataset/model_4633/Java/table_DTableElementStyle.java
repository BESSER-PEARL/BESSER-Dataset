





import java.util.List;
import java.util.ArrayList;

public class table_DTableElementStyle  {

    private boolean defaultBackgroundStyle;
    private String labelFormat;
    private boolean defaultForegroundStyle;
    private String foregroundColor;
    private int labelSize;
    private String backgroundColor;





    private table_DColumn table_dcolumn;




    private table_DLine table_dline;


    public table_DTableElementStyle(
        boolean defaultBackgroundStyle,        String labelFormat,        boolean defaultForegroundStyle,        String foregroundColor,        int labelSize,        String backgroundColor    ) {
        this.defaultBackgroundStyle = defaultBackgroundStyle;
        this.labelFormat = labelFormat;
        this.defaultForegroundStyle = defaultForegroundStyle;
        this.foregroundColor = foregroundColor;
        this.labelSize = labelSize;
        this.backgroundColor = backgroundColor;
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
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
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