





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private String FilePath;
    private String EscapeType;
    private String TextIdentifier;
    private boolean RemoveEmptyRow;
    private String RowSeparatorValue;
    private String FieldSeparatorValue;
    private String HeaderValue;
    private boolean UseLimit;
    private boolean CsvOption;
    private String RowSeparatorType;
    private boolean FirstLineCaption;
    private String TextEnclosure;
    private String Format;
    private String LimitValue;
    private String Encoding;
    private String FooterValue;
    private boolean UseHeader;
    private boolean UseFooter;
    private String EscapeChar;
    private String Server;



    public connection_FileConnection(
        String FilePath,        String EscapeType,        String TextIdentifier,        boolean RemoveEmptyRow,        String RowSeparatorValue,        String FieldSeparatorValue,        String HeaderValue,        boolean UseLimit,        boolean CsvOption,        String RowSeparatorType,        boolean FirstLineCaption,        String TextEnclosure,        String Format,        String LimitValue,        String Encoding,        String FooterValue,        boolean UseHeader,        boolean UseFooter,        String EscapeChar,        String Server    ) {
        super(
        );
        this.FilePath = FilePath;
        this.EscapeType = EscapeType;
        this.TextIdentifier = TextIdentifier;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.RowSeparatorValue = RowSeparatorValue;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.HeaderValue = HeaderValue;
        this.UseLimit = UseLimit;
        this.CsvOption = CsvOption;
        this.RowSeparatorType = RowSeparatorType;
        this.FirstLineCaption = FirstLineCaption;
        this.TextEnclosure = TextEnclosure;
        this.Format = Format;
        this.LimitValue = LimitValue;
        this.Encoding = Encoding;
        this.FooterValue = FooterValue;
        this.UseHeader = UseHeader;
        this.UseFooter = UseFooter;
        this.EscapeChar = EscapeChar;
        this.Server = Server;
    }


    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
    }
    public boolean getRemoveemptyrow() {
        return RemoveEmptyRow;
    }

    public void setRemoveemptyrow(boolean RemoveEmptyRow) {
        this.RemoveEmptyRow = RemoveEmptyRow;
    }
    public String getRowseparatorvalue() {
        return RowSeparatorValue;
    }

    public void setRowseparatorvalue(String RowSeparatorValue) {
        this.RowSeparatorValue = RowSeparatorValue;
    }
    public String getFieldseparatorvalue() {
        return FieldSeparatorValue;
    }

    public void setFieldseparatorvalue(String FieldSeparatorValue) {
        this.FieldSeparatorValue = FieldSeparatorValue;
    }
    public String getHeadervalue() {
        return HeaderValue;
    }

    public void setHeadervalue(String HeaderValue) {
        this.HeaderValue = HeaderValue;
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
    public String getRowseparatortype() {
        return RowSeparatorType;
    }

    public void setRowseparatortype(String RowSeparatorType) {
        this.RowSeparatorType = RowSeparatorType;
    }
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
    }
    public String getFormat() {
        return Format;
    }

    public void setFormat(String Format) {
        this.Format = Format;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }


}