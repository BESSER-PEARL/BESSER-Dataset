





import java.util.List;
import java.util.ArrayList;

public class component_Port extends WrapperObject {

    private boolean allowAnyDataType;
    private String interfaces;
    private boolean allowAnySubscriptionType;
    private String originalPortString;
    private String interfaceType;
    private boolean allowAnyDataflowType;
    private String subscriptionType;
    private String nameL;
    private String dataflowType;
    private String dataType;
    private boolean allowAnyInterfaceType;





    private component_Component component_component;




    private List<component_ConnectorProfile> component_connectorprofiles;




    private component_PortSynchronizer component_portsynchronizer;


    public component_Port(
        boolean allowAnyDataType,        String interfaces,        boolean allowAnySubscriptionType,        String originalPortString,        String interfaceType,        boolean allowAnyDataflowType,        String subscriptionType,        String nameL,        String dataflowType,        String dataType,        boolean allowAnyInterfaceType    ) {
        super(
        );
        this.allowAnyDataType = allowAnyDataType;
        this.interfaces = interfaces;
        this.allowAnySubscriptionType = allowAnySubscriptionType;
        this.originalPortString = originalPortString;
        this.interfaceType = interfaceType;
        this.allowAnyDataflowType = allowAnyDataflowType;
        this.subscriptionType = subscriptionType;
        this.nameL = nameL;
        this.dataflowType = dataflowType;
        this.dataType = dataType;
        this.allowAnyInterfaceType = allowAnyInterfaceType;
        this.component_connectorprofiles = new ArrayList<>();
    }

    public component_Port(
        boolean allowAnyDataType,        String interfaces,        boolean allowAnySubscriptionType,        String originalPortString,        String interfaceType,        boolean allowAnyDataflowType,        String subscriptionType,        String nameL,        String dataflowType,        String dataType,        boolean allowAnyInterfaceType        ArrayList<component_ConnectorProfile> component_connectorprofiles    ) {
        this.allowAnyDataType = allowAnyDataType;
        this.interfaces = interfaces;
        this.allowAnySubscriptionType = allowAnySubscriptionType;
        this.originalPortString = originalPortString;
        this.interfaceType = interfaceType;
        this.allowAnyDataflowType = allowAnyDataflowType;
        this.subscriptionType = subscriptionType;
        this.nameL = nameL;
        this.dataflowType = dataflowType;
        this.dataType = dataType;
        this.allowAnyInterfaceType = allowAnyInterfaceType;
        this.component_connectorprofiles = component_connectorprofiles;
    }

    public boolean getAllowanydatatype() {
        return allowAnyDataType;
    }

    public void setAllowanydatatype(boolean allowAnyDataType) {
        this.allowAnyDataType = allowAnyDataType;
    }
    public String getInterfaces() {
        return interfaces;
    }

    public void setInterfaces(String interfaces) {
        this.interfaces = interfaces;
    }
    public boolean getAllowanysubscriptiontype() {
        return allowAnySubscriptionType;
    }

    public void setAllowanysubscriptiontype(boolean allowAnySubscriptionType) {
        this.allowAnySubscriptionType = allowAnySubscriptionType;
    }
    public String getOriginalportstring() {
        return originalPortString;
    }

    public void setOriginalportstring(String originalPortString) {
        this.originalPortString = originalPortString;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public boolean getAllowanydataflowtype() {
        return allowAnyDataflowType;
    }

    public void setAllowanydataflowtype(boolean allowAnyDataflowType) {
        this.allowAnyDataflowType = allowAnyDataflowType;
    }
    public String getSubscriptiontype() {
        return subscriptionType;
    }

    public void setSubscriptiontype(String subscriptionType) {
        this.subscriptionType = subscriptionType;
    }
    public String getNamel() {
        return nameL;
    }

    public void setNamel(String nameL) {
        this.nameL = nameL;
    }
    public String getDataflowtype() {
        return dataflowType;
    }

    public void setDataflowtype(String dataflowType) {
        this.dataflowType = dataflowType;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public boolean getAllowanyinterfacetype() {
        return allowAnyInterfaceType;
    }

    public void setAllowanyinterfacetype(boolean allowAnyInterfaceType) {
        this.allowAnyInterfaceType = allowAnyInterfaceType;
    }

    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }
    public List<component_ConnectorProfile> getComponent_connectorprofiles() {
        return component_connectorprofiles;
    }

    public void addComponent_connectorprofile(Component_connectorprofile component_connectorprofile) {
        this.component_connectorprofiles.add(component_connectorprofile);
    }
    public component_PortSynchronizer getComponent_portsynchronizer() {
        return component_portsynchronizer;
    }

    public void setComponent_portsynchronizer(component_PortSynchronizer component_portsynchronizer) {
        this.component_portsynchronizer = component_portsynchronizer;
    }

}