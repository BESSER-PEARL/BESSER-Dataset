





import java.util.List;
import java.util.ArrayList;

public class component_ConnectorProfile extends IPropertyMap, WrapperObject {

    private String outportBufferLength;
    private String interfaceType;
    private String outportBufferReadTimeout;
    private boolean pushIntervalAvailable;
    private String outportBufferWriteTimeout;
    private boolean isReverse;
    private String sourceString;
    private String inportBufferEmptyPolicy;
    private String connectorId;
    private String outportBufferEmptyPolicy;
    private String targetString;
    private String dataType;
    private String inportBufferWriteTimeout;
    private String outportSerializerType;
    private String pushPolicy;
    private String inportSerializerType;
    private boolean subscriptionTypeAvailable;
    private String timestampPolicy;
    private String outportBufferFullPolicy;
    private String inportBufferFullPolicy;
    private String inportBufferLength;
    private boolean skipCountAvailable;
    private String name;
    private String inportBufferReadTimeout;
    private String subscriptionType;
    private boolean pushPolicyAvailable;
    private String pushRate;
    private String dataflowType;
    private String skipCount;



    public component_ConnectorProfile(
        String outportBufferLength,        String interfaceType,        String outportBufferReadTimeout,        boolean pushIntervalAvailable,        String outportBufferWriteTimeout,        boolean isReverse,        String sourceString,        String inportBufferEmptyPolicy,        String connectorId,        String outportBufferEmptyPolicy,        String targetString,        String dataType,        String inportBufferWriteTimeout,        String outportSerializerType,        String pushPolicy,        String inportSerializerType,        boolean subscriptionTypeAvailable,        String timestampPolicy,        String outportBufferFullPolicy,        String inportBufferFullPolicy,        String inportBufferLength,        boolean skipCountAvailable,        String name,        String inportBufferReadTimeout,        String subscriptionType,        boolean pushPolicyAvailable,        String pushRate,        String dataflowType,        String skipCount    ) {
        super(
        );
        this.outportBufferLength = outportBufferLength;
        this.interfaceType = interfaceType;
        this.outportBufferReadTimeout = outportBufferReadTimeout;
        this.pushIntervalAvailable = pushIntervalAvailable;
        this.outportBufferWriteTimeout = outportBufferWriteTimeout;
        this.isReverse = isReverse;
        this.sourceString = sourceString;
        this.inportBufferEmptyPolicy = inportBufferEmptyPolicy;
        this.connectorId = connectorId;
        this.outportBufferEmptyPolicy = outportBufferEmptyPolicy;
        this.targetString = targetString;
        this.dataType = dataType;
        this.inportBufferWriteTimeout = inportBufferWriteTimeout;
        this.outportSerializerType = outportSerializerType;
        this.pushPolicy = pushPolicy;
        this.inportSerializerType = inportSerializerType;
        this.subscriptionTypeAvailable = subscriptionTypeAvailable;
        this.timestampPolicy = timestampPolicy;
        this.outportBufferFullPolicy = outportBufferFullPolicy;
        this.inportBufferFullPolicy = inportBufferFullPolicy;
        this.inportBufferLength = inportBufferLength;
        this.skipCountAvailable = skipCountAvailable;
        this.name = name;
        this.inportBufferReadTimeout = inportBufferReadTimeout;
        this.subscriptionType = subscriptionType;
        this.pushPolicyAvailable = pushPolicyAvailable;
        this.pushRate = pushRate;
        this.dataflowType = dataflowType;
        this.skipCount = skipCount;
    }


    public String getOutportbufferlength() {
        return outportBufferLength;
    }

    public void setOutportbufferlength(String outportBufferLength) {
        this.outportBufferLength = outportBufferLength;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public String getOutportbufferreadtimeout() {
        return outportBufferReadTimeout;
    }

    public void setOutportbufferreadtimeout(String outportBufferReadTimeout) {
        this.outportBufferReadTimeout = outportBufferReadTimeout;
    }
    public boolean getPushintervalavailable() {
        return pushIntervalAvailable;
    }

    public void setPushintervalavailable(boolean pushIntervalAvailable) {
        this.pushIntervalAvailable = pushIntervalAvailable;
    }
    public String getOutportbufferwritetimeout() {
        return outportBufferWriteTimeout;
    }

    public void setOutportbufferwritetimeout(String outportBufferWriteTimeout) {
        this.outportBufferWriteTimeout = outportBufferWriteTimeout;
    }
    public boolean getIsreverse() {
        return isReverse;
    }

    public void setIsreverse(boolean isReverse) {
        this.isReverse = isReverse;
    }
    public String getSourcestring() {
        return sourceString;
    }

    public void setSourcestring(String sourceString) {
        this.sourceString = sourceString;
    }
    public String getInportbufferemptypolicy() {
        return inportBufferEmptyPolicy;
    }

    public void setInportbufferemptypolicy(String inportBufferEmptyPolicy) {
        this.inportBufferEmptyPolicy = inportBufferEmptyPolicy;
    }
    public String getConnectorid() {
        return connectorId;
    }

    public void setConnectorid(String connectorId) {
        this.connectorId = connectorId;
    }
    public String getOutportbufferemptypolicy() {
        return outportBufferEmptyPolicy;
    }

    public void setOutportbufferemptypolicy(String outportBufferEmptyPolicy) {
        this.outportBufferEmptyPolicy = outportBufferEmptyPolicy;
    }
    public String getTargetstring() {
        return targetString;
    }

    public void setTargetstring(String targetString) {
        this.targetString = targetString;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getInportbufferwritetimeout() {
        return inportBufferWriteTimeout;
    }

    public void setInportbufferwritetimeout(String inportBufferWriteTimeout) {
        this.inportBufferWriteTimeout = inportBufferWriteTimeout;
    }
    public String getOutportserializertype() {
        return outportSerializerType;
    }

    public void setOutportserializertype(String outportSerializerType) {
        this.outportSerializerType = outportSerializerType;
    }
    public String getPushpolicy() {
        return pushPolicy;
    }

    public void setPushpolicy(String pushPolicy) {
        this.pushPolicy = pushPolicy;
    }
    public String getInportserializertype() {
        return inportSerializerType;
    }

    public void setInportserializertype(String inportSerializerType) {
        this.inportSerializerType = inportSerializerType;
    }
    public boolean getSubscriptiontypeavailable() {
        return subscriptionTypeAvailable;
    }

    public void setSubscriptiontypeavailable(boolean subscriptionTypeAvailable) {
        this.subscriptionTypeAvailable = subscriptionTypeAvailable;
    }
    public String getTimestamppolicy() {
        return timestampPolicy;
    }

    public void setTimestamppolicy(String timestampPolicy) {
        this.timestampPolicy = timestampPolicy;
    }
    public String getOutportbufferfullpolicy() {
        return outportBufferFullPolicy;
    }

    public void setOutportbufferfullpolicy(String outportBufferFullPolicy) {
        this.outportBufferFullPolicy = outportBufferFullPolicy;
    }
    public String getInportbufferfullpolicy() {
        return inportBufferFullPolicy;
    }

    public void setInportbufferfullpolicy(String inportBufferFullPolicy) {
        this.inportBufferFullPolicy = inportBufferFullPolicy;
    }
    public String getInportbufferlength() {
        return inportBufferLength;
    }

    public void setInportbufferlength(String inportBufferLength) {
        this.inportBufferLength = inportBufferLength;
    }
    public boolean getSkipcountavailable() {
        return skipCountAvailable;
    }

    public void setSkipcountavailable(boolean skipCountAvailable) {
        this.skipCountAvailable = skipCountAvailable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInportbufferreadtimeout() {
        return inportBufferReadTimeout;
    }

    public void setInportbufferreadtimeout(String inportBufferReadTimeout) {
        this.inportBufferReadTimeout = inportBufferReadTimeout;
    }
    public String getSubscriptiontype() {
        return subscriptionType;
    }

    public void setSubscriptiontype(String subscriptionType) {
        this.subscriptionType = subscriptionType;
    }
    public boolean getPushpolicyavailable() {
        return pushPolicyAvailable;
    }

    public void setPushpolicyavailable(boolean pushPolicyAvailable) {
        this.pushPolicyAvailable = pushPolicyAvailable;
    }
    public String getPushrate() {
        return pushRate;
    }

    public void setPushrate(String pushRate) {
        this.pushRate = pushRate;
    }
    public String getDataflowtype() {
        return dataflowType;
    }

    public void setDataflowtype(String dataflowType) {
        this.dataflowType = dataflowType;
    }
    public String getSkipcount() {
        return skipCount;
    }

    public void setSkipcount(String skipCount) {
        this.skipCount = skipCount;
    }


}