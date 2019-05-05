from alog import debug, info, error
from mykonos.core.core import Core

class Element(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def open_notification(self, **settings):
        """ open notification of Android

        HOW TO CALL IN ROBOT FRAMEWORK

        | Open notification                  |

        with device:
        | ${device_1}=  Scan Current Device  |  ${emulator}
        | Open notification                  |  device=${device_1}

        Return:
        True or False
        """

        if 'device' in settings:
            device = settings['device']
            return device.open.notification()
        else:
            return self.device_mobile.open.notification()

    def open_quick_settings(self, **settings):
        """ open quick settingss of Android
        HOW TO CALL IN ROBOT FRAMEWORK

        | Open Quick Notification                  |

        with device:
        | ${device_1}=  Scan Current Device        |  ${emulator}
        | Open Quick Notification                  |  device=${device_1}

        Return:
        True or False
        """

        if 'device' in settings:
            device = settings['device']
            return device.open.quick_settings()
        else:
            return self.device_mobile.open.quick_settings()

    def click_element(self, *argument, **settings):
        """ click on UI base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Click Element                    | className=sample class

        with locator:
        | ${get_locator}= Get Locator       | text=sample text
        |  Click Element                    | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device  | ${emulator}
        |  Click Element                     | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator        | text=sample text
        | ${device_1}=  Scan Current Device  | ${emulator}
        |  Click Element                     | device=${device_1}    locator=${get_locator}

        Return:
        True or False
         """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).click()
            else:
                return self.device_mobile(*argument, **settings).click()

    def long_click_element(self, *argument, **settings):
        """ long click on UI base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Long Click Element                    | className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        |  Long Click Element                    | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Long Click Element                    | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Long Click Element                   | device=${device_1}    locator=${get_locator}

        Return:
        True or False
         """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.long_click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **locator).long_click()
            else:
                return self.device_mobile(*argument, **settings).long_click()


    def clear_text(self, *argument, **settings):
        """ clear text on text field base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Clear Text                            |  className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Clear Text                             | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Clear Text                            | device=${device_1}    text=sample text

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Clear Text                           | device=${device_1}    locator=${get_locator}

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.clear_text()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).clear_text()
            else:
                return self.device_mobile(*argument, **settings).clear_text()

    def input_text(self, *argument, **settings):
        """ input text on text field base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Input Text                            |  className=sample class    input=Sampling text for input

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Input Text                             | locator=${get_locator}     input=Sampling text for input

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Input Text                            | device=${device_1}    text=sample text   input=Sampling text for input

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Input Text                           | device=${device_1}    locator=${get_locator}      input=Sampling text for input

        return:
        True or False
        """
        input = settings['input']
        del settings['input']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.set_text(input)
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).set_text(input)
            else:
                return self.device_mobile(*argument, **settings).set_text(input)


    def get_text(self, *argument, **settings):
        """ get text from element base on locator
        selector support :
        text, textContains, textMatches, textStartsWith
        className, classNameMatches
        description, descriptionContains, descriptionMatches, descriptionStartsWith
        checkable, checked, clickable, longClickable
        scrollable, enabled,focusable, focused, selected
        packageName, packageNameMatches
        resourceId, resourceIdMatches
        index, instance

        HOW TO CALL IN ROBOT FRAMEWORK

        |  Get Text                              |  className=sample class

        with locator:
        | ${get_locator}= Get Locator            | text=sample text
        | Get Text                               | locator=${get_locator}

        with device:
        | ${device_1}=  Scan Current Device      | ${emulator}
        |  Get Text                              | device=${device_1}    className=sample class

        with locator and device
        | ${get_locator}= Get Locator           | text=sample text
        | ${device_1}=  Scan Current Device     | ${emulator}
        |  Get Text                             | device=${device_1}    locator=${get_locator}

        return:
        String

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info['text']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']


    def get_element_attribute(self, *argument, **settings):
        """ get element attribute using list of the elements :
        List of Elements:
         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable,
         focused, longClickable, scrollable, selected

         example :
         get_element_attribute(element="text", className="")
         """
        element = settings['element']
        del settings['element']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.info[element]
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info[element]
            else:
                return self.device_mobile(*argument, **settings).info[element]

    def click_a_point(self, *argument, **settings):
        """Click into pointer target location
        example :
        click_a_point(x=value, y=value)
        """
        if 'x' in settings and 'y' in settings:
            x = settings['x']
            y = settings['y']
            del settings['x']
            del settings['y']
        else:
            raise ValueError('pointer x or y is refused')

        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **locator).click(x, y)
        else:
            return self.device_mobile().click(x, y)

    def get_element(self, *argument, **settings):
        """ Call keyword_device_info
        and will return dictionary
        Example :
        Example_Code:orcestrator = Orcestrator(data)
        orcestrator.device_info
        Example_robot_framework:
        | ${device_info} | Device Info |
        | Log Dictionary | ${device_info}  |
        Return:
        {'currentPackageName': 'com.google.android.apps.nexuslauncher',
         'displayHeight': 1794,
         'displayRotation': 0,
         'displaySizeDpX': 411,
         'displaySizeDpY': 731,
         'displayWidth': 1080,
         'productName': 'sdk_google_phone_x86',
         'screenOn': True,
         'sdkInt': 25,
         'naturalOrientation': True}
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info
            else:
                return self.device_mobile(*argument, **settings).info

    def get_element_by_coordinate_x(self, *argument, **settings):
        """
        get element by coorditane x
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)
        right = bound['right']
        left = bound['left']
        bottom = bound['bottom']
        top = bound['top']
        elm_x = (top+bottom)+top
        return elm_x

    def get_element_by_coordinate_y(self, *argument, **settings):
        """
        get element by coorditane y
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)
        display_height = self.get_height()
        height = display_height
        left = bound['left']
        right = bound['right']
        elm_y = height-(right+left)
        return elm_y

    def count_elements(self, *argument, **settings):
        """ Count total element from the page
        - locator is used for user who want to get locator first before count element
        example :
        element = get_locator("className=name of class ")
        total_element = count_elements(locator=element)

        - device mobile is used for user who input element directly on device
        total_element = count_elements("className=name of class ")

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        else:
            return self.device_mobile(*argument, **settings).count

    def get_width(self):
        """ Get width from display of device
        example : get_width()
        return : int
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """ Get height from display of device
        example : get_height()
        return : int
        """
        get_device = self.device()
        return get_device.info['displayHeight']
