





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private String Server;
    private String FooterValue;
    private boolean RemoveEmptyRow;
    private String EscapeChar;
    private boolean UseHeader;
    private String EscapeType;
    private String Format;
    private boolean UseLimit;
    private boolean CsvOption;
    private String RowSeparatorValue;
    private boolean FirstLineCaption;
    private boolean UseFooter;
    private String FilePath;
    private String RowSeparatorType;
    private String HeaderValue;
    private String FieldSeparatorValue;
    private String TextEnclosure;
    private String LimitValue;
    private String TextIdentifier;
    private String Encoding;



    public connection_FileConnection(
        String Server,        String FooterValue,        boolean RemoveEmptyRow,        String EscapeChar,        boolean UseHeader,        String EscapeType,        String Format,        boolean UseLimit,        boolean CsvOption,        String RowSeparatorValue,        boolean FirstLineCaption,        boolean UseFooter,        String FilePath,        String RowSeparatorType,        String HeaderValue,        String FieldSeparatorValue,        String TextEnclosure,        String LimitValue,        String TextIdentifier,        String Encoding    ) {
        super(
        );
        this.Server = Server;
        this.FooterValue = FooterValue;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.EscapeChar = EscapeChar;
        this.UseHeader = UseHeader;
        this.EscapeType = EscapeType;
        this.Format = Format;
        this.UseLimit = UseLimit;
        this.CsvOption = CsvOption;
        this.RowSeparatorValue = RowSeparatorValue;
        this.FirstLineCaption = FirstLineCaption;
        this.UseFooter = UseFooter;
        this.FilePath = FilePath;
        this.RowSeparatorType = RowSeparatorType;
        this.HeaderValue = HeaderValue;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.TextEnclosure = TextEnclosure;
        this.LimitValue = LimitValue;
        this.TextIdentifier = TextIdentifier;
        this.Encoding = Encoding;
    }


    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public boolean getRemoveemptyrow() {
        return RemoveEmptyRow;
    }

    public void setRemoveemptyrow(boolean RemoveEmptyRow) {
        this.RemoveEmptyRow = RemoveEmptyRow;
    }
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
    }
    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
    }
    public String getRowseparatorvalue() {
        return RowSeparatorValue;
    }

    public void setRowseparatorvalue(String RowSeparatorValue) {
        this.RowSeparatorValue = RowSeparatorValue;
    }
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getRowseparatortype() {
        return RowSeparatorType;
    }

    public void setRowseparatortype(String RowSeparatorType) {
        this.RowSeparatorType = RowSeparatorType;
    }
    public String getHeadervalue() {
        return HeaderValue;
    }

    public void setHeadervalue(String HeaderValue) {
        this.HeaderValue = HeaderValue;
    }
    public String getFieldseparatorvalue() {
        return FieldSeparatorValue;
    }

    public void setFieldseparatorvalue(String FieldSeparatorValue) {
        this.FieldSeparatorValue = FieldSeparatorValue;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }


}