





import java.util.List;
import java.util.ArrayList;

public class component_Port extends WrapperObject {

    private boolean allowAnySubscriptionType;
    private boolean allowAnyDataflowType;
    private String dataType;
    private String interfaces;
    private boolean allowAnyInterfaceType;
    private String subscriptionType;
    private String originalPortString;
    private boolean allowAnyDataType;
    private String interfaceType;
    private String nameL;
    private String dataflowType;





    private List<component_ConnectorProfile> component_connectorprofiles;




    private component_PortSynchronizer component_portsynchronizer;




    private component_Component component_component;


    public component_Port(
        boolean allowAnySubscriptionType,        boolean allowAnyDataflowType,        String dataType,        String interfaces,        boolean allowAnyInterfaceType,        String subscriptionType,        String originalPortString,        boolean allowAnyDataType,        String interfaceType,        String nameL,        String dataflowType    ) {
        super(
        );
        this.allowAnySubscriptionType = allowAnySubscriptionType;
        this.allowAnyDataflowType = allowAnyDataflowType;
        this.dataType = dataType;
        this.interfaces = interfaces;
        this.allowAnyInterfaceType = allowAnyInterfaceType;
        this.subscriptionType = subscriptionType;
        this.originalPortString = originalPortString;
        this.allowAnyDataType = allowAnyDataType;
        this.interfaceType = interfaceType;
        this.nameL = nameL;
        this.dataflowType = dataflowType;
        this.component_connectorprofiles = new ArrayList<>();
    }

    public component_Port(
        boolean allowAnySubscriptionType,        boolean allowAnyDataflowType,        String dataType,        String interfaces,        boolean allowAnyInterfaceType,        String subscriptionType,        String originalPortString,        boolean allowAnyDataType,        String interfaceType,        String nameL,        String dataflowType        ArrayList<component_ConnectorProfile> component_connectorprofiles    ) {
        this.allowAnySubscriptionType = allowAnySubscriptionType;
        this.allowAnyDataflowType = allowAnyDataflowType;
        this.dataType = dataType;
        this.interfaces = interfaces;
        this.allowAnyInterfaceType = allowAnyInterfaceType;
        this.subscriptionType = subscriptionType;
        this.originalPortString = originalPortString;
        this.allowAnyDataType = allowAnyDataType;
        this.interfaceType = interfaceType;
        this.nameL = nameL;
        this.dataflowType = dataflowType;
        this.component_connectorprofiles = component_connectorprofiles;
    }

    public boolean getAllowanysubscriptiontype() {
        return allowAnySubscriptionType;
    }

    public void setAllowanysubscriptiontype(boolean allowAnySubscriptionType) {
        this.allowAnySubscriptionType = allowAnySubscriptionType;
    }
    public boolean getAllowanydataflowtype() {
        return allowAnyDataflowType;
    }

    public void setAllowanydataflowtype(boolean allowAnyDataflowType) {
        this.allowAnyDataflowType = allowAnyDataflowType;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }
    public String getInterfaces() {
        return interfaces;
    }

    public void setInterfaces(String interfaces) {
        this.interfaces = interfaces;
    }
    public boolean getAllowanyinterfacetype() {
        return allowAnyInterfaceType;
    }

    public void setAllowanyinterfacetype(boolean allowAnyInterfaceType) {
        this.allowAnyInterfaceType = allowAnyInterfaceType;
    }
    public String getSubscriptiontype() {
        return subscriptionType;
    }

    public void setSubscriptiontype(String subscriptionType) {
        this.subscriptionType = subscriptionType;
    }
    public String getOriginalportstring() {
        return originalPortString;
    }

    public void setOriginalportstring(String originalPortString) {
        this.originalPortString = originalPortString;
    }
    public boolean getAllowanydatatype() {
        return allowAnyDataType;
    }

    public void setAllowanydatatype(boolean allowAnyDataType) {
        this.allowAnyDataType = allowAnyDataType;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
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
    public component_Component getComponent_component() {
        return component_component;
    }

    public void setComponent_component(component_Component component_component) {
        this.component_component = component_component;
    }

}