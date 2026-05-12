





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String Separator;
    private int LimitValue;
    private boolean GetBaseDNsFromRoot;
    private String BindPassword;
    private String Host;
    private String SelectedDN;
    private String ReturnAttributes;
    private String Protocol;
    private String BaseDNs;
    private String Referrals;
    private boolean UseAuthen;
    private String EncryptionMethodName;
    private String CountLimit;
    private String BindPrincipal;
    private String Aliases;
    private String TimeOutLimit;
    private boolean UseAdvanced;
    private String Port;
    private String StorePath;
    private String Filter;
    private String Value;
    private boolean UseLimit;
    private boolean SavePassword;



    public connection_LDAPSchemaConnection(
        String Separator,        int LimitValue,        boolean GetBaseDNsFromRoot,        String BindPassword,        String Host,        String SelectedDN,        String ReturnAttributes,        String Protocol,        String BaseDNs,        String Referrals,        boolean UseAuthen,        String EncryptionMethodName,        String CountLimit,        String BindPrincipal,        String Aliases,        String TimeOutLimit,        boolean UseAdvanced,        String Port,        String StorePath,        String Filter,        String Value,        boolean UseLimit,        boolean SavePassword    ) {
        super(
        );
        this.Separator = Separator;
        this.LimitValue = LimitValue;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.BindPassword = BindPassword;
        this.Host = Host;
        this.SelectedDN = SelectedDN;
        this.ReturnAttributes = ReturnAttributes;
        this.Protocol = Protocol;
        this.BaseDNs = BaseDNs;
        this.Referrals = Referrals;
        this.UseAuthen = UseAuthen;
        this.EncryptionMethodName = EncryptionMethodName;
        this.CountLimit = CountLimit;
        this.BindPrincipal = BindPrincipal;
        this.Aliases = Aliases;
        this.TimeOutLimit = TimeOutLimit;
        this.UseAdvanced = UseAdvanced;
        this.Port = Port;
        this.StorePath = StorePath;
        this.Filter = Filter;
        this.Value = Value;
        this.UseLimit = UseLimit;
        this.SavePassword = SavePassword;
    }


    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public int getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(int LimitValue) {
        this.LimitValue = LimitValue;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
    }
    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getSelecteddn() {
        return SelectedDN;
    }

    public void setSelecteddn(String SelectedDN) {
        this.SelectedDN = SelectedDN;
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
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
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
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
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
    public boolean getUseadvanced() {
        return UseAdvanced;
    }

    public void setUseadvanced(boolean UseAdvanced) {
        this.UseAdvanced = UseAdvanced;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
    }


}