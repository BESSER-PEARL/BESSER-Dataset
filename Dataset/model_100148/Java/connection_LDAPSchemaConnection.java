





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String EncryptionMethodName;
    private boolean GetBaseDNsFromRoot;
    private String Port;
    private String Value;
    private String BindPrincipal;
    private String ReturnAttributes;
    private String CountLimit;
    private boolean SavePassword;
    private String StorePath;
    private String Filter;
    private int LimitValue;
    private String SelectedDN;
    private String TimeOutLimit;
    private String Separator;
    private boolean UseAuthen;
    private boolean UseAdvanced;
    private boolean UseLimit;
    private String Aliases;
    private String BaseDNs;
    private String Protocol;
    private String Host;
    private String BindPassword;
    private String Referrals;



    public connection_LDAPSchemaConnection(
        String EncryptionMethodName,        boolean GetBaseDNsFromRoot,        String Port,        String Value,        String BindPrincipal,        String ReturnAttributes,        String CountLimit,        boolean SavePassword,        String StorePath,        String Filter,        int LimitValue,        String SelectedDN,        String TimeOutLimit,        String Separator,        boolean UseAuthen,        boolean UseAdvanced,        boolean UseLimit,        String Aliases,        String BaseDNs,        String Protocol,        String Host,        String BindPassword,        String Referrals    ) {
        super(
        );
        this.EncryptionMethodName = EncryptionMethodName;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.Port = Port;
        this.Value = Value;
        this.BindPrincipal = BindPrincipal;
        this.ReturnAttributes = ReturnAttributes;
        this.CountLimit = CountLimit;
        this.SavePassword = SavePassword;
        this.StorePath = StorePath;
        this.Filter = Filter;
        this.LimitValue = LimitValue;
        this.SelectedDN = SelectedDN;
        this.TimeOutLimit = TimeOutLimit;
        this.Separator = Separator;
        this.UseAuthen = UseAuthen;
        this.UseAdvanced = UseAdvanced;
        this.UseLimit = UseLimit;
        this.Aliases = Aliases;
        this.BaseDNs = BaseDNs;
        this.Protocol = Protocol;
        this.Host = Host;
        this.BindPassword = BindPassword;
        this.Referrals = Referrals;
    }


    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
    }
    public String getStorepath() {
        return StorePath;
    }

    public void setStorepath(String StorePath) {
        this.StorePath = StorePath;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
    }
    public int getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(int LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getSelecteddn() {
        return SelectedDN;
    }

    public void setSelecteddn(String SelectedDN) {
        this.SelectedDN = SelectedDN;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public boolean getUseadvanced() {
        return UseAdvanced;
    }

    public void setUseadvanced(boolean UseAdvanced) {
        this.UseAdvanced = UseAdvanced;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getAliases() {
        return Aliases;
    }

    public void setAliases(String Aliases) {
        this.Aliases = Aliases;
    }
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getProtocol() {
        return Protocol;
    }

    public void setProtocol(String Protocol) {
        this.Protocol = Protocol;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
    }


}