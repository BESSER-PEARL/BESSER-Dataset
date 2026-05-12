





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String Value;
    private String SelectedDN;
    private String BindPassword;
    private String BaseDNs;
    private String Aliases;
    private String CountLimit;
    private String Separator;
    private boolean SavePassword;
    private boolean UseLimit;
    private boolean GetBaseDNsFromRoot;
    private String ReturnAttributes;
    private String Protocol;
    private String BindPrincipal;
    private boolean UseAuthen;
    private int LimitValue;
    private String Referrals;
    private String TimeOutLimit;
    private String Host;
    private boolean UseAdvanced;
    private String EncryptionMethodName;
    private String Filter;
    private String StorePath;
    private String Port;



    public connection_LDAPSchemaConnection(
        String Value,        String SelectedDN,        String BindPassword,        String BaseDNs,        String Aliases,        String CountLimit,        String Separator,        boolean SavePassword,        boolean UseLimit,        boolean GetBaseDNsFromRoot,        String ReturnAttributes,        String Protocol,        String BindPrincipal,        boolean UseAuthen,        int LimitValue,        String Referrals,        String TimeOutLimit,        String Host,        boolean UseAdvanced,        String EncryptionMethodName,        String Filter,        String StorePath,        String Port    ) {
        super(
        );
        this.Value = Value;
        this.SelectedDN = SelectedDN;
        this.BindPassword = BindPassword;
        this.BaseDNs = BaseDNs;
        this.Aliases = Aliases;
        this.CountLimit = CountLimit;
        this.Separator = Separator;
        this.SavePassword = SavePassword;
        this.UseLimit = UseLimit;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.ReturnAttributes = ReturnAttributes;
        this.Protocol = Protocol;
        this.BindPrincipal = BindPrincipal;
        this.UseAuthen = UseAuthen;
        this.LimitValue = LimitValue;
        this.Referrals = Referrals;
        this.TimeOutLimit = TimeOutLimit;
        this.Host = Host;
        this.UseAdvanced = UseAdvanced;
        this.EncryptionMethodName = EncryptionMethodName;
        this.Filter = Filter;
        this.StorePath = StorePath;
        this.Port = Port;
    }


    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getSelecteddn() {
        return SelectedDN;
    }

    public void setSelecteddn(String SelectedDN) {
        this.SelectedDN = SelectedDN;
    }
    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getAliases() {
        return Aliases;
    }

    public void setAliases(String Aliases) {
        this.Aliases = Aliases;
    }
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public String getProtocol() {
        return Protocol;
    }

    public void setProtocol(String Protocol) {
        this.Protocol = Protocol;
    }
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }
    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public int getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(int LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public boolean getUseadvanced() {
        return UseAdvanced;
    }

    public void setUseadvanced(boolean UseAdvanced) {
        this.UseAdvanced = UseAdvanced;
    }
    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
    }
    public String getStorepath() {
        return StorePath;
    }

    public void setStorepath(String StorePath) {
        this.StorePath = StorePath;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }


}