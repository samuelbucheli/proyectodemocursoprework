import React from 'react';
import classnames from 'classnames';
import styled from 'styled-components';
import { compose } from 'lodash/fp';
import { withRouter } from 'react-router-dom';
import { inject, observer } from 'mobx-react';
import debug from '@/utils/debug';

/* 引入less的两种方式, 按需使用 */
import './index.less';
import Style from './index.module.less';
import { Store } from '@/store';

const log = debug('Example/Header');

/* 样式组件, 可以通过编辑器插件进行代码提示 */
const StyledDiv = styled.div`
    color: peachpuff;
`;

interface Props {
    example: Store['example'];
}

function Header(props: Props) {
    const {
        example: { header: headerStore }
    } = props;
    log('this is a header');

    return (
        <div className={classnames(Style.container, 'header-container')}>
            <p
                className={classnames(
                    Style.containerText,
                    'header-container-text'
                )}
            >
                this is header
            </p>
            <StyledDiv>
                this is header content--
                {headerStore.content}
            </StyledDiv>
        </div>
    );
}

export default compose(
    withRouter,
    inject('example'),
    observer
)(Header);
