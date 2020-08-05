from webdriver.common.by import By




def handle_black(func):
    def warapper(*args, **kwargs):
        from page.base_page import BasePage
        instance : BasePage = args[0]
        _black_list = [
            (By.XPATH, "//*[@class='123']"),
            (By.XPATH, "//*[@class='321']")
        ]
        _max_err_num = 3
        _error_num = 0
        try:
            # 和find中一致
            element = func(*args, **kwargs)
            _error_num = 0
            return element
            # 如果元素找到，就清空error 记录
        except Exception as e:


            # 如果没找到就进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果error次数大于指定值，清空error次数 并报错
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._black_list:
                # 找这个元素对黑名单点击
                eles = instance.find(ele)
                # 找到就是大于0
                if len(eles) > 0:
                    eles[0].click()
                    # 返回自己重新调用find
                    return warapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return warapper()