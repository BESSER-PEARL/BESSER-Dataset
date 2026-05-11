





import java.util.List;
import java.util.ArrayList;

public class component_ConnectorProfile extends WrapperObject, IPropertyMap {

    private String pushPolicy;
    private String name;
    private String sourceString;
    private String inportBufferWriteTimeout;
    private boolean pushIntervalAvailable;
    private String connectorId;
    private String inportBufferEmptyPolicy;
    private String timestampPolicy;
    private String subscriptionType;
    private String pushRate;
    private String outportBufferReadTimeout;
    private String outportBufferLength;
    private boolean subscriptionTypeAvailable;
    private String targetString;
    private boolean pushPolicyAvailable;
    private String inportBufferFullPolicy;
    private String dataflowType;
    private boolean skipCountAvailable;
    private String outportBufferFullPolicy;
    private String outportBufferEmptyPolicy;
    private String inportBufferLength;
    private String interfaceType;
    private String inportBufferReadTimeout;
    private String dataType;
    private String skipCount;
    private boolean isReverse;
    private String outportBufferWriteTimeout;



    public component_ConnectorProfile(
        String pushPolicy,        String name,        String sourceString,        String inportBufferWriteTimeout,        boolean pushIntervalAvailable,        String connectorId,        String inportBufferEmptyPolicy,        String timestampPolicy,        String subscriptionType,        String pushRate,        String outportBufferReadTimeout,        String outportBufferLength,        boolean subscriptionTypeAvailable,        String targetString,        boolean pushPolicyAvailable,        String inportBufferFullPolicy,        String dataflowType,        boolean skipCountAvailable,        String outportBufferFullPolicy,        String outportBufferEmptyPolicy,        String inportBufferLength,        String interfaceType,        String inportBufferReadTimeout,        String dataType,        String skipCount,        boolean isReverse,        String outportBufferWriteTimeout    ) {
        super(
        );
        this.pushPolicy = pushPolicy;
        this.name = name;
        this.sourceString = sourceString;
        this.inportBufferWriteTimeout = inportBufferWriteTimeout;
        this.pushIntervalAvailable = pushIntervalAvailable;
        this.connectorId = connectorId;
        this.inportBufferEmptyPolicy = inportBufferEmptyPolicy;
        this.timestampPolicy = timestampPolicy;
        this.subscriptionType = subscriptionType;
        this.pushRate = pushRate;
        this.outportBufferReadTimeout = outportBufferReadTimeout;
        this.outportBufferLength = outportBufferLength;
        this.subscriptionTypeAvailable = subscriptionTypeAvailable;
        this.targetString = targetString;
        this.pushPolicyAvailable = pushPolicyAvailable;
        this.inportBufferFullPolicy = inportBufferFullPolicy;
        this.dataflowType = dataflowType;
        this.skipCountAvailable = skipCountAvailable;
        this.outportBufferFullPolicy = outportBufferFullPolicy;
        this.outportBufferEmptyPolicy = outportBufferEmptyPolicy;
        this.inportBufferLength = inportBufferLength;
        this.interfaceType = interfaceType;
        this.inportBufferReadTimeout = inportBufferReadTimeout;
        this.dataType = dataType;
        this.skipCount = skipCount;
        this.isReverse = isReverse;
        this.outportBufferWriteTimeout = outportBufferWriteTimeout;
    }


    public String getPushpolicy() {
        return pushPolicy;
    }

    public void setPushpolicy(String pushPolicy) {
        this.pushPolicy = pushPolicy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSourcestring() {
        return sourceString;
    }

    public void setSourcestring(String sourceString) {
        this.sourceString = sourceString;
    }
    public String getInportbufferwritetimeout() {
        return inportBufferWriteTimeout;
    }

    public void setInportbufferwritetimeout(String inportBufferWriteTimeout) {
        this.inportBufferWriteTimeout = inportBufferWriteTimeout;
    }
    public boolean getPushintervalavailable() {
        return pushIntervalAvailable;
    }

    public void setPushintervalavailable(boolean pushIntervalAvailable) {
        this.pushIntervalAvailable = pushIntervalAvailable;
    }
    public String getConnectorid() {
        return connectorId;
    }

    public void setConnectorid(String connectorId) {
        this.connectorId = connectorId;
    }
    public String getInportbufferemptypolicy() {
        return inportBufferEmptyPolicy;
    }

    public void setInportbufferemptypolicy(String inportBufferEmptyPolicy) {
        this.inportBufferEmptyPolicy = inportBufferEmptyPolicy;
    }
    public String getTimestamppolicy() {
        return timestampPolicy;
    }

    public void setTimestamppolicy(String timestampPolicy) {
        this.timestampPolicy = timestampPolicy;
    }
    public String getSubscriptiontype() {
        return subscriptionType;
    }

    public void setSubscriptiontype(String subscriptionType) {
        this.subscriptionType = subscriptionType;
    }
    public String getPushrate() {
        return pushRate;
    }

    public void setPushrate(String pushRate) {
        this.pushRate = pushRate;
    }
    public String getOutportbufferreadtimeout() {
        return outportBufferReadTimeout;
    }

    public void setOutportbufferreadtimeout(String outportBufferReadTimeout) {
        this.outportBufferReadTimeout = outportBufferReadTimeout;
    }
    public String getOutportbufferlength() {
        return outportBufferLength;
    }

    public void setOutportbufferlength(String outportBufferLength) {
        this.outportBufferLength = outportBufferLength;
    }
    public boolean getSubscriptiontypeavailable() {
        return subscriptionTypeAvailable;
    }

    public void setSubscriptiontypeavailable(boolean subscriptionTypeAvailable) {
        this.subscriptionTypeAvailable = subscriptionTypeAvailable;
    }
    public String getTargetstring() {
        return targetString;
    }

    public void setTargetstring(String targetString) {
        this.targetString = targetString;
    }
    public boolean getPushpolicyavailable() {
        return pushPolicyAvailable;
    }

    public void setPushpolicyavailable(boolean pushPolicyAvailable) {
        this.pushPolicyAvailable = pushPolicyAvailable;
    }
    public String getInportbufferfullpolicy() {
        return inportBufferFullPolicy;
    }

    public void setInportbufferfullpolicy(String inportBufferFullPolicy) {
        this.inportBufferFullPolicy = inportBufferFullPolicy;
    }
    public String getDataflowtype() {
        return dataflowType;
    }

    public void setDataflowtype(String dataflowType) {
        this.dataflowType = dataflowType;
    }
    public boolean getSkipcountavailable() {
        return skipCountAvailable;
    }

    public void setSkipcountavailable(boolean skipCountAvailable) {
        this.skipCountAvailable = skipCountAvailable;
    }
    public String getOutportbufferfullpolicy() {
        return outportBufferFullPolicy;
    }

    public void setOutportbufferfullpolicy(String outportBufferFullPolicy) {
        this.outportBufferFullPolicy = outportBufferFullPolicy;
    }
    public String getOutportbufferemptypolicy() {
        return outportBufferEmptyPolicy;
    }

    public void setOutportbufferemptypolicy(String outportBufferEmptyPolicy) {
        this.outportBufferEmptyPolicy = outportBufferEmptyPolicy;
    }
    public String getInportbufferlength() {
        return inportBufferLength;
    }

    public void setInportbufferlength(String inportBufferLength) {
        this.inportBufferLength = inportBufferLength;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public String getInportbufferreadtimeout() {
        return inportBufferReadTimeout;
    }

    public void setInportbufferreadtimeout(String inportBufferReadTimeout) {
        this.inportBufferReadTimeout = inportBufferReadTimeout;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getSkipcount() {
        return skipCount;
    }

    public void setSkipcount(String skipCount) {
        this.skipCount = skipCount;
    }
    public boolean getIsreverse() {
        return isReverse;
    }

    public void setIsreverse(boolean isReverse) {
        this.isReverse = isReverse;
    }
    public String getOutportbufferwritetimeout() {
        return outportBufferWriteTimeout;
    }

    public void setOutportbufferwritetimeout(String outportBufferWriteTimeout) {
        this.outportBufferWriteTimeout = outportBufferWriteTimeout;
    }


}