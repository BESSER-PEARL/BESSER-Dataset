





import java.util.List;
import java.util.ArrayList;

public class connection_LDAPSchemaConnection extends Connection {

    private boolean UseAuthen;
    private String TimeOutLimit;
    private boolean SavePassword;
    private String Referrals;
    private String Host;
    private int LimitValue;
    private String Protocol;
    private String StorePath;
    private boolean UseLimit;
    private String Aliases;
    private String BindPrincipal;
    private String EncryptionMethodName;
    private String BaseDNs;
    private String Port;
    private String Filter;
    private String CountLimit;
    private String ReturnAttributes;
    private boolean GetBaseDNsFromRoot;
    private String SelectedDN;
    private boolean UseAdvanced;
    private String Value;
    private String BindPassword;
    private String Separator;



    public connection_LDAPSchemaConnection(
        boolean UseAuthen,        String TimeOutLimit,        boolean SavePassword,        String Referrals,        String Host,        int LimitValue,        String Protocol,        String StorePath,        boolean UseLimit,        String Aliases,        String BindPrincipal,        String EncryptionMethodName,        String BaseDNs,        String Port,        String Filter,        String CountLimit,        String ReturnAttributes,        boolean GetBaseDNsFromRoot,        String SelectedDN,        boolean UseAdvanced,        String Value,        String BindPassword,        String Separator    ) {
        super(
        );
        this.UseAuthen = UseAuthen;
        this.TimeOutLimit = TimeOutLimit;
        this.SavePassword = SavePassword;
        this.Referrals = Referrals;
        this.Host = Host;
        this.LimitValue = LimitValue;
        this.Protocol = Protocol;
        this.StorePath = StorePath;
        this.UseLimit = UseLimit;
        this.Aliases = Aliases;
        this.BindPrincipal = BindPrincipal;
        this.EncryptionMethodName = EncryptionMethodName;
        this.BaseDNs = BaseDNs;
        this.Port = Port;
        this.Filter = Filter;
        this.CountLimit = CountLimit;
        this.ReturnAttributes = ReturnAttributes;
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
        this.SelectedDN = SelectedDN;
        this.UseAdvanced = UseAdvanced;
        this.Value = Value;
        this.BindPassword = BindPassword;
        this.Separator = Separator;
    }


    public boolean getUseauthen() {
        return UseAuthen;
    }

    public void setUseauthen(boolean UseAuthen) {
        this.UseAuthen = UseAuthen;
    }
    public String getTimeoutlimit() {
        return TimeOutLimit;
    }

    public void setTimeoutlimit(String TimeOutLimit) {
        this.TimeOutLimit = TimeOutLimit;
    }
    public boolean getSavepassword() {
        return SavePassword;
    }

    public void setSavepassword(boolean SavePassword) {
        this.SavePassword = SavePassword;
    }
    public String getReferrals() {
        return Referrals;
    }

    public void setReferrals(String Referrals) {
        this.Referrals = Referrals;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public int getLimitvalue() {
        return LimitValue;
    }

    public void setLimitvalue(int LimitValue) {
        this.LimitValue = LimitValue;
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
    public String getBindprincipal() {
        return BindPrincipal;
    }

    public void setBindprincipal(String BindPrincipal) {
        this.BindPrincipal = BindPrincipal;
    }
    public String getEncryptionmethodname() {
        return EncryptionMethodName;
    }

    public void setEncryptionmethodname(String EncryptionMethodName) {
        this.EncryptionMethodName = EncryptionMethodName;
    }
    public String getBasedns() {
        return BaseDNs;
    }

    public void setBasedns(String BaseDNs) {
        this.BaseDNs = BaseDNs;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getFilter() {
        return Filter;
    }

    public void setFilter(String Filter) {
        this.Filter = Filter;
    }
    public String getCountlimit() {
        return CountLimit;
    }

    public void setCountlimit(String CountLimit) {
        this.CountLimit = CountLimit;
    }
    public String getReturnattributes() {
        return ReturnAttributes;
    }

    public void setReturnattributes(String ReturnAttributes) {
        this.ReturnAttributes = ReturnAttributes;
    }
    public boolean getGetbasednsfromroot() {
        return GetBaseDNsFromRoot;
    }

    public void setGetbasednsfromroot(boolean GetBaseDNsFromRoot) {
        this.GetBaseDNsFromRoot = GetBaseDNsFromRoot;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getBindpassword() {
        return BindPassword;
    }

    public void setBindpassword(String BindPassword) {
        this.BindPassword = BindPassword;
    }
    public String getSeparator() {
        return Separator;
    }

    public void setSeparator(String Separator) {
        this.Separator = Separator;
    }


}