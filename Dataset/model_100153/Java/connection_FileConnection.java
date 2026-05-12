





import java.util.List;
import java.util.ArrayList;

public class connection_FileConnection extends Connection {

    private boolean CsvOption;
    private String FilePath;
    private String TextIdentifier;
    private String LimitValue;
    private boolean UseHeader;
    private boolean RemoveEmptyRow;
    private String Format;
    private boolean FirstLineCaption;
    private String TextEnclosure;
    private String EscapeChar;
    private String Server;
    private String RowSeparatorValue;
    private String FieldSeparatorValue;
    private String FooterValue;
    private boolean UseLimit;
    private boolean UseFooter;
    private String HeaderValue;
    private String EscapeType;
    private String Encoding;
    private String RowSeparatorType;



    public connection_FileConnection(
        boolean CsvOption,        String FilePath,        String TextIdentifier,        String LimitValue,        boolean UseHeader,        boolean RemoveEmptyRow,        String Format,        boolean FirstLineCaption,        String TextEnclosure,        String EscapeChar,        String Server,        String RowSeparatorValue,        String FieldSeparatorValue,        String FooterValue,        boolean UseLimit,        boolean UseFooter,        String HeaderValue,        String EscapeType,        String Encoding,        String RowSeparatorType    ) {
        super(
        );
        this.CsvOption = CsvOption;
        this.FilePath = FilePath;
        this.TextIdentifier = TextIdentifier;
        this.LimitValue = LimitValue;
        this.UseHeader = UseHeader;
        this.RemoveEmptyRow = RemoveEmptyRow;
        this.Format = Format;
        this.FirstLineCaption = FirstLineCaption;
        this.TextEnclosure = TextEnclosure;
        this.EscapeChar = EscapeChar;
        this.Server = Server;
        this.RowSeparatorValue = RowSeparatorValue;
        this.FieldSeparatorValue = FieldSeparatorValue;
        this.FooterValue = FooterValue;
        this.UseLimit = UseLimit;
        this.UseFooter = UseFooter;
        this.HeaderValue = HeaderValue;
        this.EscapeType = EscapeType;
        this.Encoding = Encoding;
        this.RowSeparatorType = RowSeparatorType;
    }


    public boolean getCsvoption() {
        return CsvOption;
    }

    public void setCsvoption(boolean CsvOption) {
        this.CsvOption = CsvOption;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getTextidentifier() {
        return TextIdentifier;
    }

    public void setTextidentifier(String TextIdentifier) {
        this.TextIdentifier = TextIdentifier;
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
    public String getTextenclosure() {
        return TextEnclosure;
    }

    public void setTextenclosure(String TextEnclosure) {
        this.TextEnclosure = TextEnclosure;
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
    public boolean getUsefooter() {
        return UseFooter;
    }

    public void setUsefooter(boolean UseFooter) {
        this.UseFooter = UseFooter;
    }
    public String getHeadervalue() {
        return HeaderValue;
    }

    public void setHeadervalue(String HeaderValue) {
        this.HeaderValue = HeaderValue;
    }
    public String getEscapetype() {
        return EscapeType;
    }

    public void setEscapetype(String EscapeType) {
        this.EscapeType = EscapeType;
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


}