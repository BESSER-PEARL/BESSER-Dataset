





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private String Protocol;
    private String Value;
    private String Referrals;
    private int LimitValue;
    private String Host;
    private String EncryptionMethodName;
    private String Separator;
    private String Filter;
    private boolean UseLimit;
    private String StorePath;
    private String Aliases;
    private String SelectedDN;
    private boolean UseAdvanced;
    private String CountLimit;
    private String Port;
    private String BindPassword;
    private boolean SavePassword;
    private String BaseDNs;
    private String ReturnAttributes;
    private boolean UseAuthen;
    private boolean GetBaseDNsFromRoot;
    private String TimeOutLimit;
    private String BindPrincipal;



    public connection_LDAPSchemaConnection(
        String Protocol,        String Value,        String Referrals,        int LimitValue,        String Host,        String EncryptionMethodName,        String Separator,        String Filter,        boolean UseLimit,        String StorePath,        String Aliases,        String SelectedDN,        boolean UseAdvanced,        String CountLimit,        String Port,        String BindPassword,        boolean SavePassword,        String BaseDNs,        String ReturnAttributes,        boolean UseAuthen,        boolean GetBaseDNsFromRoot,        String TimeOutLimit,        String BindPrincipal    ) {
        super(
        );
        this.Protocol = Protocol;
        this.Value = Value;
        this.Referrals = Referrals;
        this.LimitValue = LimitValue;
        this.Host = Host;
        this.EncryptionMethodName = EncryptionMethodName;
        this.Separator = Separator;
        this.Filter = Filter;
        this.UseLimit = UseLimit;
        this.StorePath = StorePath;
        this.Aliases = Aliases;
        this.SelectedDN = SelectedDN;
        this.UseAdvanced = UseAdvanced;
        this.CountLimit = CountLimit;
        this.Port = Port;
        this.BindPassword = BindPassword;
        this.SavePassword = SavePassword;
        this.BaseDNs = BaseDNs;
        this.ReturnAttributes = ReturnAttributes;
        this.UseAuthen = UseAuthen;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.TimeOutLimit = TimeOutLimit;
        this.BindPrincipal = BindPrincipal;
    }


    public String getProtocol() {
        return Protocol;
    }

    public void setProtocol(String Protocol) {
        this.Protocol = Protocol;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
    }
    public int getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(int LimitValue) {
        this.LimitValue = LimitValue;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getStorepath() {
        return StorePath;
    }

    public void setStorepath(String StorePath) {
        this.StorePath = StorePath;
    }
    public String getAliases() {
        return Aliases;
    }

    public void setAliases(String Aliases) {
        this.Aliases = Aliases;
    }
    public String getSelecteddn() {
        return SelectedDN;
    }

    public void setSelecteddn(String SelectedDN) {
        this.SelectedDN = SelectedDN;
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
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
    }
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }


}