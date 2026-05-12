





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private String FooterValue;
    private boolean UseLimit;
    private String HeaderValue;
    private String FieldSeparatorValue;
    private String EscapeChar;
    private String TextEnclosure;
    private boolean UseFooter;
    private String LimitValue;
    private boolean UseHeader;
    private String FilePath;
    private String Encoding;
    private String RowSeparatorType;
    private boolean CsvOption;
    private String EscapeType;
    private String Format;
    private String Server;
    private String RowSeparatorValue;
    private String TextIdentifier;
    private boolean RemoveEmptyRow;
    private boolean FirstLineCaption;



    public connection_FileConnection(
        String FooterValue,        boolean UseLimit,        String HeaderValue,        String FieldSeparatorValue,        String EscapeChar,        String TextEnclosure,        boolean UseFooter,        String LimitValue,        boolean UseHeader,        String FilePath,        String Encoding,        String RowSeparatorType,        boolean CsvOption,        String EscapeType,        String Format,        String Server,        String RowSeparatorValue,        String TextIdentifier,        boolean RemoveEmptyRow,        boolean FirstLineCaption    ) {
        super(
        );
        this.FooterValue = FooterValue;
        this.UseLimit = UseLimit;
        this.HeaderValue = HeaderValue;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.EscapeChar = EscapeChar;
        this.TextEnclosure = TextEnclosure;
        this.UseFooter = UseFooter;
        this.LimitValue = LimitValue;
        this.UseHeader = UseHeader;
        this.FilePath = FilePath;
        this.Encoding = Encoding;
        this.RowSeparatorType = RowSeparatorType;
        this.CsvOption = CsvOption;
        this.EscapeType = EscapeType;
        this.Format = Format;
        this.Server = Server;
        this.RowSeparatorValue = RowSeparatorValue;
        this.TextIdentifier = TextIdentifier;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.FirstLineCaption = FirstLineCaption;
    }


    public String getFootervalue() {
        return FooterValue;
    }

    public void setFootervalue(String FooterValue) {
        this.FooterValue = FooterValue;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
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
    public String getEscapechar() {
        return EscapeChar;
    }

    public void setEscapechar(String EscapeChar) {
        this.EscapeChar = EscapeChar;
    }
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
    }
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(String LimitValue) {
        this.LimitValue = LimitValue;
    }
    public boolean getUseheader() {
        return UseHeader;
    }

    public void setUseheader(boolean UseHeader) {
        this.UseHeader = UseHeader;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getRowseparatortype() {
        return RowSeparatorType;
    }

    public void setRowseparatortype(String RowSeparatorType) {
        this.RowSeparatorType = RowSeparatorType;
    }
    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
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
    public boolean getFirstlinecaption() {
        return FirstLineCaption;
    }

    public void setFirstlinecaption(boolean FirstLineCaption) {
        this.FirstLineCaption = FirstLineCaption;
    }


}