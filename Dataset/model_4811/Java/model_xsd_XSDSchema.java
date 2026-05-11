





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDSchema extends XSDScope {

    private String targetNamespace;
    private String blockDefault;
    private String elementFormDefault;
    private String schemaLocation;
    private String version;
    private String finalDefault;
    private String attributeFormDefault;
    private String document;





    private List<XSDTypeDefinition> xsdtypedefinitions;




    private List<XSDElementDeclaration> xsdelementdeclarations;




    private List<XSDIdentityConstraintDefinition> xsdidentityconstraintdefinitions;




    private List<XSDAnnotation> xsdannotations;




    private XSDSchema xsdschema;




    private XSDSchema xsdschema;




    private List<XSDSchema> xsdschemas;




    private List<XSDDiagnostic> xsddiagnostics;




    private XSDSchema xsdschema;


    public model_xsd_XSDSchema(
        String targetNamespace,        String blockDefault,        String elementFormDefault,        String schemaLocation,        String version,        String finalDefault,        String attributeFormDefault,        String document    ) {
        super(
        );
        this.targetNamespace = targetNamespace;
        this.blockDefault = blockDefault;
        this.elementFormDefault = elementFormDefault;
        this.schemaLocation = schemaLocation;
        this.version = version;
        this.finalDefault = finalDefault;
        this.attributeFormDefault = attributeFormDefault;
        this.document = document;
        this.xsdtypedefinitions = new ArrayList<>();
        this.xsdelementdeclarations = new ArrayList<>();
        this.xsdidentityconstraintdefinitions = new ArrayList<>();
        this.xsdannotations = new ArrayList<>();
        this.xsdschemas = new ArrayList<>();
        this.xsddiagnostics = new ArrayList<>();
    }

    public model_xsd_XSDSchema(
        String targetNamespace,        String blockDefault,        String elementFormDefault,        String schemaLocation,        String version,        String finalDefault,        String attributeFormDefault,        String document        ArrayList<XSDTypeDefinition> xsdtypedefinitions,        ArrayList<XSDElementDeclaration> xsdelementdeclarations,        ArrayList<XSDIdentityConstraintDefinition> xsdidentityconstraintdefinitions,        ArrayList<XSDAnnotation> xsdannotations,        ArrayList<XSDSchema> xsdschemas,        ArrayList<XSDDiagnostic> xsddiagnostics    ) {
        this.targetNamespace = targetNamespace;
        this.blockDefault = blockDefault;
        this.elementFormDefault = elementFormDefault;
        this.schemaLocation = schemaLocation;
        this.version = version;
        this.finalDefault = finalDefault;
        this.attributeFormDefault = attributeFormDefault;
        this.document = document;
        this.xsdtypedefinitions = xsdtypedefinitions;
        this.xsdelementdeclarations = xsdelementdeclarations;
        this.xsdidentityconstraintdefinitions = xsdidentityconstraintdefinitions;
        this.xsdannotations = xsdannotations;
        this.xsdschemas = xsdschemas;
        this.xsddiagnostics = xsddiagnostics;
    }

    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }
    public String getBlockdefault() {
        return blockDefault;
    }

    public void setBlockdefault(String blockDefault) {
        this.blockDefault = blockDefault;
    }
    public String getElementformdefault() {
        return elementFormDefault;
    }

    public void setElementformdefault(String elementFormDefault) {
        this.elementFormDefault = elementFormDefault;
    }
    public String getSchemalocation() {
        return schemaLocation;
    }

    public void setSchemalocation(String schemaLocation) {
        this.schemaLocation = schemaLocation;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFinaldefault() {
        return finalDefault;
    }

    public void setFinaldefault(String finalDefault) {
        this.finalDefault = finalDefault;
    }
    public String getAttributeformdefault() {
        return attributeFormDefault;
    }

    public void setAttributeformdefault(String attributeFormDefault) {
        this.attributeFormDefault = attributeFormDefault;
    }
    public String getDocument() {
        return document;
    }

    public void setDocument(String document) {
        this.document = document;
    }

    public List<XSDTypeDefinition> getXsdtypedefinitions() {
        return xsdtypedefinitions;
    }

    public void addXsdtypedefinition(Xsdtypedefinition xsdtypedefinition) {
        this.xsdtypedefinitions.add(xsdtypedefinition);
    }
    public List<XSDElementDeclaration> getXsdelementdeclarations() {
        return xsdelementdeclarations;
    }

    public void addXsdelementdeclaration(Xsdelementdeclaration xsdelementdeclaration) {
        this.xsdelementdeclarations.add(xsdelementdeclaration);
    }
    public List<XSDIdentityConstraintDefinition> getXsdidentityconstraintdefinitions() {
        return xsdidentityconstraintdefinitions;
    }

    public void addXsdidentityconstraintdefinition(Xsdidentityconstraintdefinition xsdidentityconstraintdefinition) {
        this.xsdidentityconstraintdefinitions.add(xsdidentityconstraintdefinition);
    }
    public List<XSDAnnotation> getXsdannotations() {
        return xsdannotations;
    }

    public void addXsdannotation(Xsdannotation xsdannotation) {
        this.xsdannotations.add(xsdannotation);
    }
    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }
    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }
    public List<XSDSchema> getXsdschemas() {
        return xsdschemas;
    }

    public void addXsdschema(Xsdschema xsdschema) {
        this.xsdschemas.add(xsdschema);
    }
    public List<XSDDiagnostic> getXsddiagnostics() {
        return xsddiagnostics;
    }

    public void addXsddiagnostic(Xsddiagnostic xsddiagnostic) {
        this.xsddiagnostics.add(xsddiagnostic);
    }
    public XSDSchema getXsdschema() {
        return xsdschema;
    }

    public void setXsdschema(XSDSchema xsdschema) {
        this.xsdschema = xsdschema;
    }

}