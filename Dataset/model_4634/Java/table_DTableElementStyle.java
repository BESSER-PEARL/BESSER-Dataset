





import java.util.List;
import java.util.ArrayList;

public class table_DTableElementStyle  {

    private String backgroundColor;
    private boolean defaultForegroundStyle;
    private boolean defaultBackgroundStyle;
    private String labelFormat;
    private String foregroundColor;
    private int labelSize;





    private table_DColumn table_dcolumn;




    private table_DLine table_dline;


    public table_DTableElementStyle(
        String backgroundColor,        boolean defaultForegroundStyle,        boolean defaultBackgroundStyle,        String labelFormat,        String foregroundColor,        int labelSize    ) {
        this.backgroundColor = backgroundColor;
        this.defaultForegroundStyle = defaultForegroundStyle;
        this.defaultBackgroundStyle = defaultBackgroundStyle;
        this.labelFormat = labelFormat;
        this.foregroundColor = foregroundColor;
        this.labelSize = labelSize;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
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
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
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