





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String Separator;
    private String Aliases;
    private String TimeOutLimit;
    private boolean UseAuthen;
    private String Filter;
    private String BindPassword;
    private String BaseDNs;
    private String BindPrincipal;
    private boolean SavePassword;
    private String SelectedDN;
    private String Host;
    private String Protocol;
    private String StorePath;
    private String Value;
    private String EncryptionMethodName;
    private String CountLimit;
    private String Referrals;
    private boolean UseLimit;
    private String ReturnAttributes;
    private String Port;
    private boolean UseAdvanced;
    private boolean GetBaseDNsFromRoot;
    private int LimitValue;



    public connection_LDAPSchemaConnection(
        String Separator,        String Aliases,        String TimeOutLimit,        boolean UseAuthen,        String Filter,        String BindPassword,        String BaseDNs,        String BindPrincipal,        boolean SavePassword,        String SelectedDN,        String Host,        String Protocol,        String StorePath,        String Value,        String EncryptionMethodName,        String CountLimit,        String Referrals,        boolean UseLimit,        String ReturnAttributes,        String Port,        boolean UseAdvanced,        boolean GetBaseDNsFromRoot,        int LimitValue    ) {
        super(
        );
        this.Separator = Separator;
        this.Aliases = Aliases;
        this.TimeOutLimit = TimeOutLimit;
        this.UseAuthen = UseAuthen;
        this.Filter = Filter;
        this.BindPassword = BindPassword;
        this.BaseDNs = BaseDNs;
        this.BindPrincipal = BindPrincipal;
        this.SavePassword = SavePassword;
        this.SelectedDN = SelectedDN;
        this.Host = Host;
        this.Protocol = Protocol;
        this.StorePath = StorePath;
        this.Value = Value;
        this.EncryptionMethodName = EncryptionMethodName;
        this.CountLimit = CountLimit;
        this.Referrals = Referrals;
        this.UseLimit = UseLimit;
        this.ReturnAttributes = ReturnAttributes;
        this.Port = Port;
        this.UseAdvanced = UseAdvanced;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.LimitValue = LimitValue;
    }


    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public String getAliases() {
        return Aliases;
    }

    public void setAliases(String Aliases) {
        this.Aliases = Aliases;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
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
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
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
    public String getProtocol() {
        return Protocol;
    }

    public void setProtocol(String Protocol) {
        this.Protocol = Protocol;
    }
    public String getStorepath() {
        return StorePath;
    }

    public void setStorepath(String StorePath) {
        this.StorePath = StorePath;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public boolean getUseadvanced() {
        return UseAdvanced;
    }

    public void setUseadvanced(boolean UseAdvanced) {
        this.UseAdvanced = UseAdvanced;
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


}