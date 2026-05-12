





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private boolean RemoveEmptyRow;
    private String Format;
    private boolean FirstLineCaption;
    private String TextIdentifier;
    private boolean UseHeader;
    private String LimitValue;
    private String EscapeType;
    private String FooterValue;
    private String Encoding;
    private String EscapeChar;
    private boolean UseFooter;
    private String TextEnclosure;
    private String RowSeparatorType;
    private String HeaderValue;
    private String Server;
    private String RowSeparatorValue;
    private String FilePath;
    private boolean CsvOption;
    private boolean UseLimit;
    private String FieldSeparatorValue;



    public connection_FileConnection(
        boolean RemoveEmptyRow,        String Format,        boolean FirstLineCaption,        String TextIdentifier,        boolean UseHeader,        String LimitValue,        String EscapeType,        String FooterValue,        String Encoding,        String EscapeChar,        boolean UseFooter,        String TextEnclosure,        String RowSeparatorType,        String HeaderValue,        String Server,        String RowSeparatorValue,        String FilePath,        boolean CsvOption,        boolean UseLimit,        String FieldSeparatorValue    ) {
        super(
        );
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.Format = Format;
        this.FirstLineCaption = FirstLineCaption;
        this.TextIdentifier = TextIdentifier;
        this.UseHeader = UseHeader;
        this.LimitValue = LimitValue;
        this.EscapeType = EscapeType;
        this.FooterValue = FooterValue;
        this.Encoding = Encoding;
        this.EscapeChar = EscapeChar;
        this.UseFooter = UseFooter;
        this.TextEnclosure = TextEnclosure;
        this.RowSeparatorType = RowSeparatorType;
        this.HeaderValue = HeaderValue;
        this.Server = Server;
        this.RowSeparatorValue = RowSeparatorValue;
        this.FilePath = FilePath;
        this.CsvOption = CsvOption;
        this.UseLimit = UseLimit;
        this.FieldSeparatorValue = FieldSeparatorValue;
    }


    public boolean getRemoveemptyrow() {
        return RemoveEmptyRow;
    }

    public void setRemoveemptyrow(boolean RemoveEmptyRow) {
        this.RemoveEmptyRow = RemoveEmptyRow;
    }
    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
    }
    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
    }
    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
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
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getRowseparatorvalue() {
        return RowSeparatorValue;
    }

    public void setRowseparatorvalue(String RowSeparatorValue) {
        this.RowSeparatorValue = RowSeparatorValue;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getFieldseparatorvalue() {
        return FieldSeparatorValue;
    }

    public void setFieldseparatorvalue(String FieldSeparatorValue) {
        this.FieldSeparatorValue = FieldSeparatorValue;
    }


}