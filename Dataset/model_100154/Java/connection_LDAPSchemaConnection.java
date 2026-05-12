





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String BindPassword;
    private String ReturnAttributes;
    private String SelectedDN;
    private String Host;
    private boolean GetBaseDNsFromRoot;
    private int LimitValue;
    private String Referrals;
    private String Separator;
    private String BaseDNs;
    private String BindPrincipal;
    private String Protocol;
    private String Aliases;
    private String Value;
    private boolean UseAuthen;
    private String EncryptionMethodName;
    private boolean UseLimit;
    private boolean UseAdvanced;
    private String CountLimit;
    private String TimeOutLimit;
    private String Filter;
    private boolean SavePassword;
    private String StorePath;
    private String Port;



    public connection_LDAPSchemaConnection(
        String BindPassword,        String ReturnAttributes,        String SelectedDN,        String Host,        boolean GetBaseDNsFromRoot,        int LimitValue,        String Referrals,        String Separator,        String BaseDNs,        String BindPrincipal,        String Protocol,        String Aliases,        String Value,        boolean UseAuthen,        String EncryptionMethodName,        boolean UseLimit,        boolean UseAdvanced,        String CountLimit,        String TimeOutLimit,        String Filter,        boolean SavePassword,        String StorePath,        String Port    ) {
        super(
        );
        this.BindPassword = BindPassword;
        this.ReturnAttributes = ReturnAttributes;
        this.SelectedDN = SelectedDN;
        this.Host = Host;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.LimitValue = LimitValue;
        this.Referrals = Referrals;
        this.Separator = Separator;
        this.BaseDNs = BaseDNs;
        this.BindPrincipal = BindPrincipal;
        this.Protocol = Protocol;
        this.Aliases = Aliases;
        this.Value = Value;
        this.UseAuthen = UseAuthen;
        this.EncryptionMethodName = EncryptionMethodName;
        this.UseLimit = UseLimit;
        this.UseAdvanced = UseAdvanced;
        this.CountLimit = CountLimit;
        this.TimeOutLimit = TimeOutLimit;
        this.Filter = Filter;
        this.SavePassword = SavePassword;
        this.StorePath = StorePath;
        this.Port = Port;
    }


    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public String getSelecteddn() {
        return SelectedDN;
    }

    public void setSelecteddn(String SelectedDN) {
        this.SelectedDN = SelectedDN;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
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
    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }
    public String getProtocol() {
        return Protocol;
    }

    public void setProtocol(String Protocol) {
        this.Protocol = Protocol;
    }
    public String getAliases() {
        return Aliases;
    }

    public void setAliases(String Aliases) {
        this.Aliases = Aliases;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public boolean getUseadvanced() {
        return UseAdvanced;
    }

    public void setUseadvanced(boolean UseAdvanced) {
        this.UseAdvanced = UseAdvanced;
    }
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
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
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }


}